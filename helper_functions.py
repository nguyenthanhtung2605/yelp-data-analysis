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

#Initialize a spark session.
def init_spark():
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    return spark

def json_to_dataframe(json_filename):


    spark = init_spark()
    target_df = spark.read.json(json_filename)

    return target_df


def review_by_user(json_filename, user_id):
    target_df = json_to_dataframe(json_filename)

    output = target_df.filter(target_df.user_id == user_id)

    return output


def review_of_business(json_filename, business_id):
    target_df = json_to_dataframe(json_filename)

    output = target_df.filter(target_df.business_id == business_id)

    return output


def most_useful_review_by_user(json_filename, user_id):
    target_df = json_to_dataframe(json_filename)

    output = target_df.filter(target_df.user_id == user_id).orderBy(desc("useful"))

    return output


