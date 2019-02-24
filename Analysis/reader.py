# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pyspark.rdd import RDD
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import asc

def init_spark():
    spark = SparkSession \
        .builder \
        .appName("SOEN 499 project: Yelp data analysis") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    return spark

def read_json(filename):
    spark = init_spark()
    data = spark.read.json(filename)
    
    return data

def review_by_user(filename, userID):
    data = read_json(filename)
    
    output = data.filter( data.user_id == userID)
    
    return output

def review_of_business(filename, businessID):
    data = read_json(filename)
    
    output = data.filter( data.user_id == businessID)
    
    return output

def most_useful_review_by_user(filename, userID):
    data = read_json(filename)
    
    output = data.filter( data.user_id == userID).orderBy(desc("useful"))
    
    return output

print(most_useful_review_by_user("../../data/yelp_academic_dataset_review.json", "hG7b0MtEbXx5QzbzE6C_VA"))