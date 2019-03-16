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
from pyspark.sql.functions import col


from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD
from math import radians, sin, cos, acos


def get_canada_business(business_df, all_province):
    canada_business_df = business_df.filter(business_df.state.isin(all_province))
    canada_business_df.show()
    return canada_business_df

def get_business_info(business_id):
    target_df = json_to_dataframe("../data/yelp_academic_dataset_business.json")

    return output

def postal_code_distance(postal_code1, postal_code2):
    spark = init_spark()
    
    postal_code_df = spark.read.csv("../data/tbl-postal-code.csv", header="true")
    
    postal_1 = postal_code_df.filter(postal_code_df["PostalCode"] == postal_code1.replace(" ",""))
    postal_2 = postal_code_df.filter(postal_code_df["PostalCode"] == postal_code2.replace(" ",""))
    
    lat_postal_1 = radians(float(toCSVLineRDD(postal_1.select("Latitude").rdd)))
    lon_postal_1 = radians(float(toCSVLineRDD(postal_1.select("Longitude").rdd)))
    
    lat_postal_2 = radians(float(toCSVLineRDD(postal_2.select("Latitude").rdd)))
    lon_postal_2 = radians(float(toCSVLineRDD(postal_2.select("Longitude").rdd)))
    
    distance = 6371.01 * acos(sin(lat_postal_1)*sin(lat_postal_2) +
                              cos(lat_postal_1)*cos(lat_postal_2)*cos(lon_postal_1 - lon_postal_2))
    
    return distance

def business_around_5_km(target_id, canadian_business):
    business_info = get_business_info(target_id)
    business_postal_code = business_info.select("postal_code")
    
    #will change when method done @@@@@@@@@@@@@
    canadian_business = json_to_dataframe("../data/yelp_academic_dataset_business.json")\
                                            .filter("state" == "ON")

    
    return business_postal_code.show()
