import os
import sys
import time
import random
import pyspark
from pyspark.rdd import RDD
from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import desc, size, max

from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD

def interests(review_df, n, s, c):
    '''
    Using the same FP-Growth algorithm, write a script that computes 
    the interest of association rules (interest = |confidence - 
    frequency(consequent)|; note the absolute value)  obtained using 
    min support <s> and min confidence <c> (parameters of the FP-Growth 
    model), and prints the first <n> rules sorted by (1) descending 
    antecedent size in association rule, and (2) descending interest.

    Return value: a CSV string.
    Test: tests/test_interests.py
    '''
    spark = init_spark()
    
    userId_training = review_df.rdd.map(lambda x: x.user_id).distinct().sortBy(lambda x: x).zipWithIndex().collectAsMap()
    
    review_rating_format_rdd = review_df.rdd.map(lambda x: Row(user_id = int(userId_training[x.user_id]), items = [x.business_id]))
    
    temp_df = spark.createDataFrame(review_rating_format_rdd).select('user_id','items')
    
    
    reduce_review_rdd = temp_df.rdd.reduceByKey(lambda x,y: list(set(x+y)))
    print(reduce_review_rdd.take(3))
    
    
    review_rating_format_df = spark.createDataFrame(reduce_review_rdd, ['id', 'items'])
    review_rating_format_df.show()
    #fpGrowth model
    fpGrowth = FPGrowth(itemsCol="items", numPartitions = n,  minSupport=s, minConfidence=c )
    model = fpGrowth.fit(review_rating_format_df)
    
    model.associationRules.show()
    
    #take out column required for output
    frequency = model.freqItemsets.orderBy(size(model.freqItemsets[0]))
    association_rules = model.associationRules.orderBy(size(model.associationRules[0]).desc(), model.associationRules[2].desc())
    
    final_df = association_rules.join(frequency, association_rules.consequent == frequency.items, "left_outer")
    final_df = final_df.select("antecedent","consequent","confidence","items","freq")
    
    #calculate interest based on provided formula
    final_df = final_df.withColumn("interest", pyspark.sql.functions.abs(final_df.confidence - final_df.freq/review_rating_format_df.count()))    
    output = final_df.orderBy(size(final_df[0]).desc(), final_df[5].desc()).limit(n).rdd
    
    return output.take(5)