# YELP Restaurant Data Analysis and Recommendation 

Thanh Tung Nguyen (#:40042891)
Huy Tran (#:40023289)

## 1. ABSTRACT

When it comes to convenience, efficiency and safety, subway has become one of the most chosen forms of transport for people in metropolis. Yet passengers do not have many reliable sources to locate their destination except for subway broadcasts because popular localization services (e.g. Global Positioning System (GPS) and wireless localization technologies) are often unavailable underground. Therefore, we propose MetroEar, a precise subway destination alarm application for smartphones. MetroEar records ambient contextual sound by smartphone microphones, and infers the state of passengers (including stop, running, and interchange) during a subway trip. Based on the states, MetroEar further provides alarm services when approaching near a pre-set location so that passengers can focus on their interest such as listening to music, reading books, or taking a nap. The app works perfectly on major smartphones and tablets running on the most popular operating systems Android.

## 2. INTRODUCTION

This proposal is designed to suggest solutions for the unavailability of popular localization services and uselessness of mobile location and accelerometer sensors in the context of underground commute. Metro has proved its efficiency and convenience by increasing numbers of passengers. However, these passengers often cannot access to popular localization services due to the semi-closed environment of subway tunnel, blocking GPS and wireless signals. To track underground passengers, previous work either relies on a static subway timetable [1] to improve the detection accuracy, or only provides partial tracking services (i.e., stop and running of metros) [1]. However, the actual metro arrival time can vary dramatically from the timetable across zones and periods. Also, transferring time at interchange stations is missing, which is important for passengers to plan trips.

In order to tackle the above drawbacks, we propose MetroEye, a mobile service for accurate metro trip tracking. MetroEye records ambient sounds using smartphone microphones, and infers three important states during a whole subway trip: (1) Moving, the state that a passenger is on a running train. (2) Interchanging, the state that a passenger at an interchange. (3) Stopping, the state that a passenger is on a train halting at a station. These movement statuses will provide a mechanism for the application to trigger a wake cup alarm to subway passengers.

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


* **Canadian Postal Codes** - *4 GB* - [Posal Code Matrix] (https://fusiontables.google.com/DataSource?docid=1H_cl-oyeG4FDwqJUTeI_aGKmmkJdPDzRNccp96M&hl=en_US&pli=1) 
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

When it comes to convenience, efficiency and safety, subway has become one of the most chosen forms of transport for people in metropolis. Yet passengers do not have many reliable sources to locate their destination except for subway broadcasts because popular localization services (e.g. Global Positioning System (GPS) and wireless localization technologies) are often unavailable underground. Therefore, we propose MetroEar, a precise subway destination alarm application for smartphones. MetroEar records ambient contextual sound by smartphone microphones, and infers the state of passengers (including stop, running, and interchange) during a subway trip. Based on the states, MetroEar further provides alarm services when approaching near a pre-set location so that passengers can focus on their interest such as listening to music, reading books, or taking a nap. The app works perfectly on major smartphones and tablets running on the most popular operating systems Android.


## 5. DISCUSSION

When it comes to convenience, efficiency and safety, subway has become one of the most chosen forms of transport for people in metropolis. Yet passengers do not have many reliable sources to locate their destination except for subway broadcasts because popular localization services (e.g. Global Positioning System (GPS) and wireless localization technologies) are often unavailable underground. Therefore, we propose MetroEar, a precise subway destination alarm application for smartphones. MetroEar records ambient contextual sound by smartphone microphones, and infers the state of passengers (including stop, running, and interchange) during a subway trip. Based on the states, MetroEar further provides alarm services when approaching near a pre-set location so that passengers can focus on their interest such as listening to music, reading books, or taking a nap. The app works perfectly on major smartphones and tablets running on the most popular operating systems Android.



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

