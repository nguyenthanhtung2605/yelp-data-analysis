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

def is_canada_user(user_id, review_df):
    user_list_df = review_df.select('user_id')
    distinct_user_id_list = user_list_df.distinct().collect()
    output = True if user_id in distinct_user_id_list else False
    return output

def get_canada_user(user_df):
    user_df = user_df.withColumn('is_canada', is_canada_user(user_df.user_id,review_df))
    canada_user_df = user_df.filter(user_df.is_canada == True)
    return canada_user_df


def get_top_n_users(number_n, canada_user_df):

    #take top n most review user id
    canada_user_by_review_df = canada_user_df.orderBy(["review_count"], descending = [1])
    top_n_users = canada_user_by_review_df.take(n)
    return top_n_users

def pick_n_random_users(number_n, top_n_users):
    random_n_users_list = top_n_users.rdd.takeSample(False, number_n, seed = 0)[0]
    random_n_users = list()
    for each in random_n_users_list:
        random_n_users.append(each['user_id'])
    return random_n_users

