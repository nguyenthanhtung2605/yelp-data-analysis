import os
import sys
from pyspark.rdd import RDD
from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import desc
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

from helper_functions import json_to_dataframe, toCSVLineRDD
from json_to_review import review_by_user

def user_current_city(user_id):   
    #take business_id of review comment
    review_of_user = review_by_user(user_id)
    business_id_of_review = review_of_user.select("business_id")
    
    #take out current city by most appearance 
    business_df = json_to_dataframe("../data/yelp_academic_dataset_business.json")
    business_id_by_user = business_df.join(business_id_of_review,\
                                      "business_id", 'inner')
    
    user_top_business = business_id_by_user.groupBy("city").count().orderBy(desc("count")).limit(1)
    user_curr_city = user_top_business.select("city")
    
    return toCSVLineRDD(user_curr_city.rdd)
    
def user_top_5_postal_code(user_id):   
    #take business_id of review comment
    review_of_user = review_by_user(user_id)
    business_id_of_review = review_of_user.select("business_id")
    
    #take out top 5 postal code by most appearance in descending order
    business_df = json_to_dataframe("../data/yelp_academic_dataset_business.json")
    business_id_by_user = business_df.join(business_id_of_review,\
                                      "business_id", 'inner')
    
    user_top_5_business = business_id_by_user.groupBy("postal_code").count().orderBy(desc("count")).limit(5)
    user_top_5_postal_codes = user_top_5_business.select("postal_code")
    
    return toCSVLineRDD(user_top_5_postal_codes.rdd).split()

#print (user_top_5_postal_code("bLbSNkLggFnqwNNzzq-Ijw"))