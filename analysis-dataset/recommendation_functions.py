import os
import sys
from math import sqrt
from pyspark.rdd import RDD
from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import desc
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql.types import FloatType
from pyspark.sql.functions import col,abs

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
# Added for not having stack traces when binding to SparkUI

from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD

def basic_als_recommender(review_df, seed):
    '''
    This function must print the RMSE of recommendations obtained
    through ALS collaborative filtering, similarly to the example at
    http://spark.apache.org/docs/latest/ml-collaborative-filtering.html
    The training ratio must be 80% and the test ratio must be 20%. The
    random seed used to sample the training and test sets (passed to
    ''DataFrame.randomSplit') is an argument of the function. The seed
    must also be used to initialize the ALS optimizer (use
    *ALS.setSeed()*). The following parameters must be used in the ALS
    optimizer:
    - maxIter: 5
    - rank: 70
    - regParam: 0.01
    - coldStartStrategy: 'drop'
    Test file: tests/test_basic_als.py
    '''    
    spark = init_spark()
    
    userId_training = review_df.rdd.map(lambda x: x.user_id).distinct().sortBy(lambda x: x).zipWithIndex().collectAsMap()
    businessId_training = review_df.rdd.map(lambda x: x.business_id).distinct().sortBy(lambda x: x).zipWithIndex().collectAsMap()
    
    review_rating_format_rdd = review_df.rdd.map(lambda x: Row(user_id = int(userId_training[x.user_id]), 
                                                        business_id = int(businessId_training[x.business_id]), 
                                                        stars = x.stars,
                                                        original_user_id = x.user_id,
                                                        original_business_id = x.business_id))
    
    review_rating_format_df = spark.createDataFrame(review_rating_format_rdd)
    
    (training, test) = review_rating_format_df.randomSplit([0.8, 0.2],seed=seed)
    
    als = ALS(maxIter=10, rank=70, regParam=0.01, userCol="user_id", itemCol="business_id", ratingCol="stars",
              coldStartStrategy="drop")
    model = als.fit(training)

    # Evaluate the model by computing the RMSE on the test data
    predictions = model.transform(test)
    predictions.orderBy('prediction',ascending = False).show()
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="stars",
                                    predictionCol="prediction")
    output_rmse = evaluator.evaluate(predictions)

    return output_rmse

def global_average_recommender(review_df, seed):
    '''
    This function must print the RMSE of recommendations obtained
    through global average, that is, the predicted rating for each
    user-movie pair must be the global average computed in the previous
    task. Training and test
    sets should be determined as before. You can add a column to an existing DataFrame with function *.withColumn(...)*.
    Test file: tests/test_global_average_recommender.py
    '''
# =============================================================================
#     out = review_df.groupby().mean('stars').collect()[0][0]
#     test_with_avg = review_df.withColumn('prediction', lit(out))
#     
#     evaluator = RegressionEvaluator(metricName="rmse", labelCol="stars",predictionCol="prediction")
#     output_rmse = evaluator.evaluate(test_with_avg)
# =============================================================================
    (training, test) = review_df.randomSplit([0.8, 0.2],seed=seed)

    rating_mean = training.groupby().mean('stars').collect()[0][0]
        
    global_average = rating_mean
    test_with_avg = test.withColumn('prediction', lit(global_average))
    print(test_with_avg.orderBy('stars', ascending = False).select('business_id').rdd.take(5))
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="stars",predictionCol="prediction")
    output_rmse = evaluator.evaluate(test_with_avg)

    return output_rmse

def als_with_bias_recommender(review_df, seed):
    '''
    This function must return the RMSE of recommendations obtained 
    using ALS + biases. Your ALS model should make predictions for *i*, 
    the user-item interaction, then you should recompute the predicted 
    rating with the formula *i+user_mean+item_mean-m* (*m* is the 
    global rating). The RMSE should compare the original rating column 
    and the predicted rating column.  Training and test sets should be 
    determined as before. Your ALS model should use the same parameters 
    as before and be initialized with the random seed passed as 
    parameter. Test file: tests/test_als_with_bias_recommender.py
    '''
    spark = init_spark()
    
    userId_training = review_df.rdd.map(lambda x: x.user_id).distinct().sortBy(lambda x: x).zipWithIndex().collectAsMap()
    businessId_training = review_df.rdd.map(lambda x: x.business_id).distinct().sortBy(lambda x: x).zipWithIndex().collectAsMap()
    
    review_rating_format_rdd = review_df.rdd.map(lambda x: Row(user_id = int(userId_training[x.user_id]), 
                                                        business_id = int(businessId_training[x.business_id]), 
                                                        stars = x.stars,
                                                        original_user_id = x.user_id,
                                                        original_business_id = x.business_id))
    
    review_rating_format_df = spark.createDataFrame(review_rating_format_rdd)
    
    (training, test) = review_rating_format_df.randomSplit([0.8, 0.2],seed=seed)

    rating_mean = training.groupby().mean('stars').collect()[0][0]
        
    global_average = rating_mean

    user_mean = training.groupby('user_id').mean('stars')
    user_mean = user_mean.withColumnRenamed('avg(stars)', 'user_mean')
    
    item_mean = training.groupby('business_id').mean('stars')
    item_mean = item_mean.withColumnRenamed('avg(stars)', 'item_mean')

    output = training
    output = output.join(user_mean, "user_id", 'inner')
    output = output.join(item_mean, "business_id", 'inner')
    output = output.select("user_id", "business_id", "stars", "user_mean", "item_mean")

    output = output.withColumn('user_item_interaction', 
                               output.stars - (output.user_mean + output.item_mean - global_average))
    
    als = ALS(maxIter=10, rank=70, regParam=0.01, userCol="user_id", itemCol="business_id", ratingCol="stars",
              coldStartStrategy="drop")
    model_with_user_item_interaction = als.fit(output)
    predictions = model_with_user_item_interaction.transform(test)
    predictions = predictions.join(user_mean, "user_id", 'inner')
    predictions = predictions.join(item_mean, "business_id", 'inner')
    predictions = predictions.select("user_id","business_id","stars","prediction",
                                     "user_mean","item_mean")
    
    new_output = predictions.withColumn("new_prediction", predictions.prediction
                                        + predictions.user_mean + predictions.item_mean - global_average)
    
    #new_output.show()
    
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="stars",
                                    predictionCol="new_prediction")
    output_rmse = evaluator.evaluate(new_output)
    
    return output_rmse