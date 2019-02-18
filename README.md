# YELP Restaurant Data Analysis and Recommendation 

* **Thanh Tung Nguyen (#:40042891)** 

* **Huy Nguyen (#:40023289)** 

## 1. ABSTRACT

Before going out for a meal, Yelp has been one of the most popular choice for customers to check for restaurants quality. However, customers cannot fully optimize their experience with Yelp if they do not know restaurants's name or address beforehand (e.g Ones might just want to look up for food nearby instead of having to travel in a cold windy snow night). Thus, we propose Yelp!Local to tackle this problems. Yelp!Local will analyze data from the official Yelp dataset just released in 2019 and give out recommend restaurant nearby in Montreal city, as well as suggestion of most-often-visit restaurants smiliar taste customer on Yelp.
 
## 2. INTRODUCTION

Yelp!Local is designed to be the solution for the unavailability of to search specific area of Yelp. Although Yelp has been successful with its massive dataset of restaurants of many cities around the world, users are unable to enjoy its service fully with difficulty when trying to search restaurants near their current position. Yelp!Local will give out a list of recommended restaurants for users with an estimate of distance of travel to each of them. Also, when user choose a restaurant, it will suggest a list of other restaurants based on the most frequent visited place from those who go to the restaurant.

In order to achieve the goal, we have to set up a distance formula to calculate travel distance between users and each restaurant that matched the search,as well as develop an algorithm to search and suggest.

**Context** 

Being the type of being who usually go out to eat with friends, we frequently use both Yelp to find good restaurants around us. Although Yelp has a good database and reliable reviews with photos from millions of users, it doesn't provide any ability to narrow search around our current location. Thus, it would be nice to be able to perform local search on Yelp.

**Objectives**

We are insipred by that idea to create a simple console interface application to help Yelp gains local search function. The application will be able to not only gives recommendation based on location but also suggest similar resturants that may invoke interest from users. We will attempt to apply our understanding from this course on recommendation systems and frequent itemsets to develop an algorithm to achieve this goal.

**Problem to Solve**

Having said that, we need to identify main obstacles stopping us from achieving the goal. Firstly, prediction for similar clients has one major disadvantage is locality. With the limitation of not knowing the type of restaurants in Yelp public dataset, it is impossible to find similar taste reviewers from different city. Thus, we ought to figure out how to give recommendation when a user look up postal codes outside of his/her living city. 
Secondly, in order to impliment frequent itemsets, the public dataset of Yelp also pose another probblem: it doesn't track how many time each users check-in each restaurants. Consequently, we have to figure out criteria to do substitute the number of visiting the restaurant in our algorithm. 

**Related Work**

So far, no project that are realatably noted.

## 3. MATERIALS AND METHODS

### 3.1 Materials

* **Dataset** - *4 GB* - [Yelp Dataset](https://www.kaggle.com/yelp-dataset/yelp-dataset)

A trove of reviews, businesses, users, tips, and check-in data.

```
yelp_academic_dataset_business.json (131.87 MB)
yelp_academic_dataset_checkin.json (389.87 MB)
yelp_academic_dataset_review.json (4.98 GB)
yelp_academic_dataset_tip.json (233.21 MB)
yelp_academic_dataset_user.json (2.32 GB)
```
These data files will be processed and converted to tabular-format data files.


* **Canadian Postal Codes - Google Fusion Tables** - *48.8 MB* - [Canadian Postal Codes](https://fusiontables.google.com/DataSource?docid=1H_cl-oyeG4FDwqJUTeI_aGKmmkJdPDzRNccp96M&hl=en_US&pli=1) 

Calculate the great circle distance and midpoint between two latitude/longitude points

```
canadian-postal-codes (48.8 MB)
```

### 3.2 Methods

**Technologies** 

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

**Algorithms** 

And repeat

```
until finished
```

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

