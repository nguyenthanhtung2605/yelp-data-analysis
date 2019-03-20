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
from pyspark.sql.types import FloatType
from pyspark.sql.functions import udf
from pyspark.sql.functions import col

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
# Added for not having stack traces when binding to SparkUI

from helper_functions import json_to_dataframe, init_spark, toCSVLineRDD
from math import radians, sin, cos, acos, sqrt,atan2


def get_canada_business(business_df, all_province):
    canada_business_df = business_df.filter(business_df.state.isin(all_province))
    canada_business_df.show()
    return canada_business_df

def get_business_info(business_id):
    target_df = json_to_dataframe("../data/yelp_academic_dataset_business.json")
    output = target_df.filter(target_df.business_id == business_id)
    return output

def get_postal_code_distance(latitude_input, longitude_input, latitude_dfrow, longitude_dfrow):

    latitude_ptc1 = radians(float(latitude_input))
    longitude_ptc1 = radians(float(longitude_input))
    latitude_ptc2 = radians(float(str(latitude_dfrow).replace("\n","").strip()))
    longitude_ptc2 = radians(float(str(longitude_dfrow).replace("\n","").strip()))

    # radius = 6371.01 # km
    # dlat = radians(lat2-lat1)
    # dlon = radians(lon2-lon1)
    # a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) \
    # * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
    # c = 2 * atan2(sqrt(a), sqrt(1-a))
    # distance = radius * c
    distance = 6371.01 * acos(sin(latitude_ptc1)*sin(latitude_ptc2) +
                              cos(latitude_ptc1)*cos(latitude_ptc2)*cos(longitude_ptc1 - longitude_ptc2))
    return distance


def get_ptcode_within_perimeter(input_ptcode, input_distance, canada_ptcode_df):
    input_ptcode_strip = input_ptcode.replace(' ', '')
    ptc_input_row = canada_ptcode_df.filter(canada_ptcode_df['postal_code'] == str(input_ptcode_strip))
    latitude_ptc_input = float(str(toCSVLineRDD(ptc_input_row.select('fl_latitude').rdd)).replace("\n",""))
    longitude_ptc_input = float(str(toCSVLineRDD(ptc_input_row.select('fl_longitude').rdd)).replace("\n",""))

    distance_udf = udf(get_postal_code_distance, FloatType())

    # ptcode_distance_df_added1 = canada_ptcode_df.withColumn('added_latitude',lit(latitude_ptc_input))
    # ptcode_distance_df_added2 = ptcode_distance_df_added1.withColumn('added_longitude',lit(longitude_ptc_input))


    # ptcode_distance_df = canada_ptcode_df.withColumn('target_distance',
    #                         distance_udf(ptcode_distance_df_added2.added_latitude,ptcode_distance_df_added2.added_longitude
    #                                      ,ptcode_distance_df_added2.fl_latitude
    #                                      ,ptcode_distance_df_added2.fl_longitude))

    ptcode_distance_df = canada_ptcode_df.withColumn('target_distance',
                            distance_udf(lit(latitude_ptc_input),lit(longitude_ptc_input)
                                         ,canada_ptcode_df.fl_latitude
                                         ,canada_ptcode_df.fl_longitude))
    ptcode_distance_df.show()
    ptcodes_within_perimeter = ptcode_distance_df.filter(ptcode_distance_df.target_distance < input_distance)
    ptcodes_within_perimeter.show()
    ptcodes_within_perimeter_dict = ptcodes_within_perimeter.select('postal_code').collect()
    ptcodes_in_perimeter_list = list(map(lambda x: x['postal_code'], ptcodes_within_perimeter_dict))
    print (len(ptcodes_in_perimeter_list))

    return ptcodes_in_perimeter_list

def canada_business_in_perimeter_df(business_df, ptcodes_in_perimeter_list):
    canada_business_in_perimeter_df = business_df.filter(business_df.postal_code.isin(ptcodes_in_perimeter_list))
    canada_business_in_perimeter_df.show()
    return canada_business_in_perimeter_df