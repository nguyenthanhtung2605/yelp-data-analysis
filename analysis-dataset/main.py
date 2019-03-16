import helper_functions as hf
import json_to_business as jb
import json_to_review as jr
import json_to_users as ju
import json_to_checkin as jc


canada_postal_df = hf.csv_to_dataframe('../data/tbl-postal-code.csv')
business_df = hf.json_to_dataframe('../data/yelp_academic_dataset_business.json')
review_df = hf.json_to_dataframe('../data/yelp_academic_dataset_review.json')
users_df = hf.json_to_dataframe('../data/yelp_academic_dataset_user.json')

all_province = [ "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "YT" ]

# >>> 01-AO: Application introduce 5 random Yelp users with in top 100 users with most review counts  <<
## generate canada business dataframe from original yelp business dataframe
canada_business_df = jb.get_canada_business(business_df, all_province)

## generate canada business review dataframe from original yelp review dataframe
canada_business_review_df = jr.get_canada_business_review(review_df, canada_business_df)

## generate canada user dataframe from original yelp user dataframe
canada_user_df = ju.get_canada_user(users_df, canada_business_review_df)

## generate top 100 user dataframe from canada user dataframe
top_100_users = ju.get_top_n_users(100, canada_user_df)
# print(top_100_users)

## pick 5 random users from top 100 user dataframe
five_random_user = ju.pick_n_random_users(5, top_100_users)

print('Please select one of 5 random Yelp Canada users displayed below:\n')
for each in five_random_user:
    print (str(each)+'\n')


# name = raw_input("What is your name? ")