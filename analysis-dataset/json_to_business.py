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

from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD
from math import radians, sin, cos, acos


def is_canada_postal_code(postal_code, postal_df):
    postal_df = postal_df.select('PostalCode')
    distinct_postal_list = postal_df.distinct().collect()
    output = True if postal_code in distinct_postal_list else False
    return output

def get_canada_business(business_df):
    business_df = business_df.withColumn('is_canada', is_canada_postal_code(business_df.postal_code,postal_df))
    canada_business_df = business_df.filter(business_df.is_canada == True)
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
                                            
    business_within_5_km = canadian_business.flatMap(lambda row: row\
                                                     if postal_code_distance())
    
    return business_postal_code.show()

print (business_around_5_km("68dUKd8_8liJ7in4aWOSEA"))
