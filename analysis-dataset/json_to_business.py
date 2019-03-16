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

def is_canada_postal_code(postal_code, postal_df):
    postal_df = postal_df.select('PostalCode')
    distinct_postal_list = postal_df.distinct().collect()
    output = True if postal_code in distinct_postal_list else False
    return output

def get_canada_business(business_df):
    business_df = business_df.withColumn('is_canada', is_canada_postal_code(business_df.postal_code,postal_df))
    canada_business_df = business_df.filter(business_df.is_canada == True)
    return canada_business_df



