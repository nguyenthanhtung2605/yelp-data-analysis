# YELP Restaurant Data Analysis and Recommendation 

* **Thanh Tung Nguyen (#:40042891)** 

* **Huy Nguyen (#:40023289)** 

## 1. ABSTRACT

Before going out for a meal, Yelp has been one of the most popular choice for customers to check for restaurants quality. However, customers cannot fully optimize their experience with Yelp if they do not know restaurants's name or address beforehand (e.g Ones might just want to look up for food nearby instead of having to travel in a cold windy snow night). Thus, we propose Yelp!Local to tackle this problems. Yelp!Local will analyze data from the official Yelp dataset just released in 2019 and give out recommend restaurant nearby in Montreal city, as well as suggestion of taste sharing Yelp users frequently visits in that area.
 
## 2. INTRODUCTION

Yelp!Local is designed to be the solution for the unavailability of to search specific area of Yelp. Although Yelp has been successful with its massive dataset of restaurants of many cities around the world, users are unable to enjoy its service fully with difficulty when trying to search restaurants near their current position. Yelp!Local will give out a list of recommendation restaurants for users with an estimate of distance of travel to each of them. 

In order to achieve the goal, we have to set up a distance formula to calculate travel distance between users and each restaurant that matched the search. This means we need the longtitude and lattitude of all restaurants in Yelp's dataset and also user current location.
Luckily, Yelp not only has the address of every restaurant but also its longitude and latitude. Hence, we decided to trust these value and use it for our calculation.
**Context** 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

**Objectives**

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

**Presentation**

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.

**Problem to Solve**

Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere pssimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.

**Related Work**

Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

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

