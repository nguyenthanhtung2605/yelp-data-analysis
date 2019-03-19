import os
import sys
import random
from pyspark.rdd import RDD
from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import desc
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

from helper_functions import json_to_dataframe, toCSVLineRDD

def get_top_n_canada_users(number_n, canada_business_review_df):
    user_list_by_count_df = canada_business_review_df.groupBy("user_id").count().orderBy(desc("count"))
    top_n_canada_users_dict = user_list_by_count_df.select("user_id").take(number_n)
    top_n_canada_users_list = list(map(lambda x: x['user_id'], top_n_canada_users_dict))
    print (top_n_canada_users_list)
    return top_n_canada_users_list

def pick_n_random_users(number_n, top_n_canada_users_list):
    random_n_users_list = random.choices(top_n_canada_users_list, k=number_n)
    order = 0
    for each in random_n_users_list:
        order += 1
        print (str(order) +'. ' + str(each) + '\n')
    return random_n_users_list

def get_business_id_list_of_user(user_id,review_df):
    user_review_df = review_df.filter(review_df.user_id == user_id)
    user_review_df = user_review_df.select("business_id")
    business_id_list_of_user = user_review_df.collect()
    business_id_list_of_user = list(map(lambda x : x['business_id'], business_id_list_of_user))
    return business_id_list_of_user


def current_city_of_user(user_id, business_id_list_of_user,business_df):

    business_id_by_user_df = business_df.filter(business_df.business_id.isin(business_id_list_of_user))
    user_top_business = business_id_by_user_df.groupBy("city").count().orderBy(desc("count")).take(1)
    user_current_city = user_top_business[0]['city']
    print('The current city of the selected user ' + user_id + ' is :\n'+user_current_city)
    return user_current_city
    
def user_top_5_postal_code(user_id, number_n, business_id_list_of_user,business_df):

    business_id_by_user_df = business_df.filter(business_df.business_id.isin(business_id_list_of_user))
    user_top_n_business_by_count = business_id_by_user_df.groupBy("postal_code").count().orderBy(desc("count"))

    user_top_n_business_list = user_top_n_business_by_count.select("postal_code").take(number_n)

    user_top_n_postal_codes = list(map(lambda x: x['postal_code'], user_top_n_business_list))
    print (user_top_n_postal_codes)
    order = 0
    print('The top five most visited postal code of the selected user ' + user_id + ' are :\n')

    for each in user_top_n_postal_codes:
        order += 1
        print(str(order) +'. ' + str(each) + '\n')
    return user_top_n_postal_codes

