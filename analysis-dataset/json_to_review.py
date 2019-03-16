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

def review_by_user(user_id):
    target_df = json_to_dataframe("../data/yelp_academic_dataset_review.json")

    output = target_df.filter(target_df.user_id == user_id)

    return output