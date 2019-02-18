# YELP Restaurant Data Analysis and Recommendation 

* **Thanh Tung Nguyen (#:40042891)** 

* **Huy Nguyen (#:40023289)** 

## 1. ABSTRACT

Before going out for a meal, Yelp has been one of the most popular choice for customers to check for restaurants quality. However, customers cannot fully optimize their experience with Yelp if they do not know restaurants's name or address beforehand (e.g Ones might just want to look up for food nearby instead of having to travel in a cold windy snow night). Thus, we propose Yelp!Local to tackle this problems. Yelp!Local will analyze data from the official Yelp dataset just released in 2019 and give out recommend restaurant nearby in Montreal city, as well as suggestion of most-often-visit restaurants smiliar taste customer on Yelp.
 
## 2. INTRODUCTION

Yelp!Local is designed to be the solution for the unavailability of to search specific area of Yelp. Although Yelp has been successful with its massive dataset of restaurants of many cities around the world, users are unable to enjoy its service fully with difficulty when trying to search restaurants near their current position. Yelp!Local will give out a list of recommended restaurants for users with an estimate of distance of travel to each of them. Also, when user choose a restaurant, it will suggest a list of other restaurants based on the most frequent visited place from those who go to the restaurant.

In order to achieve the goal, we have to set up a distance formula to calculate travel distance between users and each restaurant that matched the search,as well as develop an algorithm to search and suggest.

**Context** 

Being the type of people who usually go out to eat with friends, we frequently use both Yelp to find good restaurants around us. Although Yelp has a good database and reliable reviews with photos from millions of users, it doesn't provide any ability to narrow search around our current location. Thus, it would be nice to be able to perform local search on Yelp and get most useful recommendations of go-to restaurants.

**Objectives**

We are insipred by that idea to create a simple console interface application to provide users with useful recommendations. The application will be able to not only give recommendation based on locations but also other method of suggestion that may invoke interest from users. We will attempt to apply our understanding from this course on recommendation systems and frequent itemsets to develop an algorithm to achieve this goal.

**Problem to Solve**

Having said that, we need to identify main obstacles stopping us from achieving the goal. Firstly, prediction for similar clients has one major disadvantage is locality. With the limitation of not knowing the type of restaurants in Yelp public dataset, it is impossible to find similar taste reviewers from different city. Thus, we ought to figure out how to give recommendation when a user look up postal codes outside of his/her living city. 

Secondly and hopefully the last, the public dataset of Yelp also pose another probblem: it doesn't track how many time each users check-in each restaurants. Consequently, in order to impliment frequent itemsets, we have to figure out criteria to do substitute the number of visiting the restaurant in our algorithm. 

**Related Work**

So far, no project that are realatably noted.

## 3. MATERIALS AND METHODS

### 3.1 Materials

* **Dataset** - *4 GB* - [Yelp Dataset](https://www.kaggle.com/yelp-dataset/yelp-dataset)


```
(YELP01) yelp_academic_dataset_business.json (131.87 MB)

Data fields in scope:

business_id:1SWheh84yJXfytovILXOAQ
name:Arizona Biltmore Golf Club
address:2818 E Camino Acequia Drive
city:Phoenix
state:AZ
postal_code:85016
latitude:33.5221425
longitude:-112.0184807
stars:3
review_count:5

```

```
(YELP02) yelp_academic_dataset_checkin.json (389.87 MB)
business_id:--1UhMGODdWsrMastO9DZw
date:2016-04-26 19:49:16, 2016-08-30 18:36:57, 2016-10-15 02:45:18

```
```
(YELP03) yelp_academic_dataset_review.json (4.98 GB)

review_id:Q1sbwvVQXV2734tPgoKj4Q
user_id:hG7b0MtEbXx5QzbzE6C_VA
business_id:ujmEBvifdJM6h6RLv4wQIg
stars:1
useful:6
```

```
(YELP04) yelp_academic_dataset_user.json (2.32 GB)
user_id:l6BmjZMeQD3rDxWUbiAiow
name:Rashmi
review_count:95
useful:84
friends:c78V-rj8NQcQjOI8KP3UEA, alRMgPcngYSCJ5naFRBz5g, ajcnq75Z5xxkvUSmmJ1bCg
average_stars:4.03
```
These data files will be processed and converted to tabular-format data files.


* **Canadian Postal Codes - Google Fusion Tables** - *48.8 MB* - [Canadian Postal Codes](https://fusiontables.google.com/DataSource?docid=1H_cl-oyeG4FDwqJUTeI_aGKmmkJdPDzRNccp96M&hl=en_US&pli=1) 

Calculate the great circle distance and midpoint between two latitude/longitude points

```
(LOPC) canadian-postal-codes (48.8 MB)
PostalCode: A0A0A0
FSA: A0A
Latitude: 48.56745
Longitude: -54.843225
PlaceName: Gander
FSA1: A
FSA-Province: 10
AreaType: Rural
```

### 3.2 Methods

**Technologies** 
For this project, asides from the requirement of using Python and Apache Spark, we will possibly use Pandas library and scikit-learn if necessary.

**Algorithms** 

Our application's simplified process is as below:

01-AO: Application introduce 5 random Yelp users with in top 100 users with most review counts

02-UI: User selects 1 of the random 5 credentials

03-AO: Application shows the user's current location (City) and top 5 most reviewed postal codes of the user.

04-UI: User enter the postal code of their desired location (arbitrary or by suggestion) in Canada

05-AO: System displays the postal codes within 5-kilometer diameter and their associated restaurants. 

06-A0: Application recommends top 10 restaurants with priorities as follows:

       + by maxtrix completion
       + by most visited
       + by most rated
       + by most reviewed
       + by shortest distance

07-UI: User selects one of the recommendations.

08-AO: System shows top-5 restaurants (frequent itemset) reviewed by most users who also rated the selected restaurant.

With the objectives is to feed data to each activity within the simplified process above. We maps the activities with the their related data set. Please see below:

01-A0: (YELP04) yelp_academic_dataset_user.json --> to find top 100 users with most review counts
02-UI: None noted
03-AO: 1st (YELP03) yelp_academic_dataset_review.json --> to group business_id (restaurants) by user_id
       2rd (YELP01) yelp_academic_dataset_business.json --> to map user_id with postal codes and city (using business_id) then find the the city and top 5 postal codes
04-UI: None noted
05-AO: 1st (LOPC) canadian-postal-codes --> to compute the distance between the input postal code with all postal codes in the list using latitudes and longtitudes --> then filter the postal code with distances equal or less than 5 kilometers.
       2rd (YELP01) yelp_academic_dataset_business.json --> to map the postal codes with their associated restaurants (using postal code)
06-AO: Take the dataframe from 05-A0 and for "matrix completion recommendations" we map the users who rated the restaurants in the dataframe and apply user-user colloborative filterings to recommend.
07-UI: None noted
08-AO: (YELP03) yelp_academic_dataset_review.json --> to find the top-5 business_id by applying frequent itemset algorithm.
       (YELP01) yelp_academic_dataset_business --> to map the business_id with the restaurants' names and addresses.

## 4. RESULTS

To be provided after finishing project.


## 5. DISCUSSION

To be provided after finishing project.



### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

