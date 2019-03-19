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
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf

from helper_functions import json_to_dataframe

def is_canada_business(business_id, business_df):
    business_list_df = business_df.select('business_id')
    distinct_business_id_list = business_list_df.distinct().collect()
    output = True if business_id in distinct_business_id_list else False
    return output

def get_canada_business_review(review_df, canada_business_df):
    canada_business_df = canada_business_df.select('business_id')
    distinct_canada_business_id_list_dict = canada_business_df.distinct().collect()
    distinct_canada_business_id_list = list(map(lambda x : x['business_id'], distinct_canada_business_id_list_dict))
    canada_review_df = review_df.filter(review_df.business_id.isin(distinct_canada_business_id_list))
    canada_review_df.show()
    return canada_review_df


