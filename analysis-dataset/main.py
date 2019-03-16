import helper_functions as hf
import json_to_business as jb
import json_to_review as jr
import json_to_users as ju
import json_to_checkin as jc


postal_df = hf.csv_to_dataframe('../data/tbl-postal-code.csv')
business_df = hf.json_to_dataframe('../data/yelp_academic_dataset_business.json')
review_df = hf.json_to_dataframe('../data/yelp_academic_dataset_review.json')
users_df = hf.json_to_dataframe('../data/yelp_academic_dataset_user.json')

print (ju.pick_n_random_users(5,users_df))