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

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD
from math import radians, sin, cos, acos


def get_canada_business(business_df, all_province):
    canada_business_df = business_df.filter(business_df.state.isin(all_province))
    canada_business_df.show()
    return canada_business_df

def get_business_info(business_id):
    target_df = json_to_dataframe("../data/yelp_academic_dataset_business.json")
    output = target_df.filter(target_df.business_id == business_id)
    return output

def postal_code_distance(ptcode1, ptcode2, canada_ptcode_df):
    
    ptc1 = canada_ptcode_df.filter(canada_ptcode_df['PostalCode'] == str(ptcode1))
    ptc2 = canada_ptcode_df.filter(canada_ptcode_df['PostalCode'] == str(ptcode2))
    
    latitude_ptc1 = radians(float(toCSVLineRDD(ptc1.select("Latitude").rdd)))
    longitude_ptc2 = radians(float(toCSVLineRDD(ptc1.select("Longitude").rdd)))
    
    lat_postal_2 = radians(float(toCSVLineRDD(ptc2.select("Latitude").rdd)))
    lon_postal_2 = radians(float(toCSVLineRDD(ptc2.select("Longitude").rdd)))
    
    distance = 6371.01 * acos(sin(latitude_ptc1)*sin(lat_postal_2) +
                              cos(latitude_ptc1)*cos(lat_postal_2)*cos(longitude_ptc2 - lon_postal_2))
    
    return distance

def get_ptcode_within_perimeter(selected_ptcode, input_distance, canada_ptcode_df):
    business_info = get_business_info(target_id)
    business_postal_code = business_info.select("postal_code")
    string_business_postal_code = toCSVLineRDD(business_postal_code.rdd).strip()
    
    #will change when method done @@@@@@@@@@@@@
    canadian_business = json_to_dataframe("../data/yelp_academic_dataset_business.json")
    canadian_business = canadian_business.filter(canadian_business["state"] == "ON")\

    postal_code_distance_udf = udf(lambda postal_code: "close" 
                                   if postal_code_distance(string_business_postal_code, postal_code) <=5 
                                   else "far", StringType())
    
    canadian_business = canadian_business.withColumn('user_item_interaction', 
                                                     postal_code_distance_udf(canadian_business.postal_code))
    

    return canadian_business

