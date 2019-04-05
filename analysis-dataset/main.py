import helper_functions as hf
import json_to_business as jb
import json_to_review as jr
import json_to_users as ju
import json_to_checkin as jc
from pyspark.sql.functions import col, trim

import recommendation_functions as rf
import frequent_itemset as fi
import time
canada_ptcode_df_original = hf.csv_to_dataframe('../data/tbl-postal-code.csv')
trim_df1 = canada_ptcode_df_original.withColumn('TrimPostalCode',trim(canada_ptcode_df_original.PostalCode))
trim_df2 = trim_df1.withColumn('TrimLatitude',trim(trim_df1.Latitude))
trim_df3 = trim_df2.withColumn('TrimLongitude',trim(trim_df2.Longitude))
trim_df4 = trim_df3.withColumn('FloatLatitude',trim_df3.TrimLatitude.cast('float'))
trim_df5 = trim_df4.withColumn('FloatLongitude',trim_df4.TrimLongitude.cast('float'))
trim_df6 = trim_df5.withColumnRenamed("TrimPostalCode", "postal_code").withColumnRenamed\
    ("FloatLatitude", "fl_latitude").withColumnRenamed("TrimLongitude", "fl_longitude")
canada_ptcode_df = trim_df6.select(['postal_code','fl_latitude','fl_longitude'])

business_df = hf.json_to_dataframe('../data/yelp_academic_dataset_business.json')
review_df = hf.json_to_dataframe('../data/yelp_academic_dataset_review.json').select('review_id', 'user_id', 'business_id', 'stars')
users_df = hf.json_to_dataframe('../data/yelp_academic_dataset_user.json')

all_province = [ "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "YT" ]

# >>> 01-AO: Application introduce 5 random Yelp users with in top 100 users with most review counts  <<
## generate canada business dataframe from original yelp business dataframe
canada_business_df = jb.get_canada_business(business_df, all_province)
print (canada_business_df.count())
## generate canada business review dataframe from original yelp review dataframe
canada_business_review_df = jr.get_canada_business_review(review_df, canada_business_df)
print (canada_business_review_df.count())
## generate top 100 user dataframe from canada user dataframe
top_100_users = ju.get_top_n_canada_users(100, canada_business_review_df)
# print(top_100_users)

print('Please select one of 5 random Yelp Canada users displayed below:\n')
## pick 5 random users from top 100 user dataframe
five_random_user = ju.pick_n_random_users(5, top_100_users)


'''
# >>> 02-UI: User selects 1 of the random 5 credentials <<

choosen_user_number = input("What is your selection? Please enter 1 to 5 :")
selected_user = five_random_user[choosen_user_number - 1]


selected_user = 'tWBLn4k1M7PLBtAtwAg73g'

# >>> 03-AO: Application shows the user's current location (City) and top 5 most reviewed postal codes of the user <<

business_id_list_of_user = ju.get_business_id_list_of_user(selected_user,review_df)

ju.current_city_of_user(selected_user, business_id_list_of_user,business_df)

top_five_most_visited_postal_codes = ju.user_top_5_postal_code(selected_user, 5, business_id_list_of_user,business_df)

choosen_postal_code_number = input("What is your selection? Please enter 1 to 5 :")
selected_postal_code = five_random_user[choosen_postal_code_number - 1]
'''
'''
start = time.time()
selected_postal_code = 'M8X 1E9'

ptcodes_within_perimeter_list = jb.get_ptcode_within_perimeter(selected_postal_code, 3, canada_ptcode_df)
canada_business_in_perimeter_df = jb.canada_business_in_perimeter_df(business_df, ptcodes_within_perimeter_list)

canadian_business_in_perimeter_id_df = canada_business_in_perimeter_df.select('business_id').withColumnRenamed('business_id','businessId')
canada_business_review_df = review_df.join(canadian_business_in_perimeter_id_df, review_df.business_id == canadian_business_in_perimeter_id_df.businessId, 'inner').drop('businessId')

#print(rf.basic_als_recommender(canada_business_review_df,123))
#print(rf.global_average_recommender(canada_business_review_df,123))
#print(rf.als_with_bias_recommender(canada_business_review_df,123))
print(fi.interests(canada_business_review_df,15, 0.1, 0.1))

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
'''