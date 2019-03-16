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

from helper_functions import json_to_dataframe

def most_useful_review_by_user(json_filename, user_id):
    target_df = json_to_dataframe(json_filename)

    output = target_df.filter(target_df.user_id == user_id).orderBy(desc("useful"))

    return output

def take_random_top_100_user():
    target_df = json_to_dataframe("../data/yelp_academic_dataset_review.json")
    
    #take top 100 most comment users id
    top_100_users = target_df.groupBy("user_id").count().orderBy(desc("count")).limit(100)
    
    #random 5 users from top 100
    random_5_users = top_100_users.rdd.takeSample(False, 5, seed = 0)
    
    output = random_5_users
    
    return output