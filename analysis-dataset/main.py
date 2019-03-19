import helper_functions as hf
import json_to_business as jb
import json_to_review as jr
import json_to_users as ju
import json_to_checkin as jc


# canada_postal_df = hf.csv_to_dataframe('../data/tbl-postal-code.csv')
business_df = hf.json_to_dataframe('../data/yelp_academic_dataset_business.json')
review_df = hf.json_to_dataframe('../data/yelp_academic_dataset_review.json')
# users_df = hf.json_to_dataframe('../data/yelp_academic_dataset_user.json')

all_province = [ "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "YT" ]
'''
# >>> 01-AO: Application introduce 5 random Yelp users with in top 100 users with most review counts  <<
## generate canada business dataframe from original yelp business dataframe
canada_business_df = jb.get_canada_business(business_df, all_province)

## generate canada business review dataframe from original yelp review dataframe
canada_business_review_df = jr.get_canada_business_review(review_df, canada_business_df)

## generate top 100 user dataframe from canada user dataframe
top_100_users = ju.get_top_n_canada_users(100, canada_business_review_df)
# print(top_100_users)

print('Please select one of 5 random Yelp Canada users displayed below:\n')
## pick 5 random users from top 100 user dataframe
five_random_user = ju.pick_n_random_users(5, top_100_users)



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

selected_postal_code = 'M8X 1E9'
