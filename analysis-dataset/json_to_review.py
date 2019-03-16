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

<<<<<<< HEAD
=======
def review_by_user(user_id):
    target_df = json_to_dataframe("../data/yelp_academic_dataset_review.json")
>>>>>>> 517d439f1a00f16b681e852ccac865d7824a6929

def is_canada_business(business_id, business_df):
    business_list_df = business_df.select('business_id')
    distinct_business_id_list = business_list_df.distinct().collect()
    output = True if business_id in distinct_business_id_list else False
    return output


def get_canada_business_review(review_df):
    review_df = review_df.withColumn('is_canada', is_canada_business(review_df.business_id,business_df))
    canada_review_df = review_df.filter(review_df.is_canada == True)
    return canada_review_df





#
# def review_by_user(json_filename, user_id):
#     target_df = json_to_dataframe(json_filename)
#
#     output = target_df.filter(target_df.user_id == user_id)
#
#     return output