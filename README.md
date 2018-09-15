# Blog
#### One MInute Pitch app created as an Independent Project on 07/09/2018
#### Author: **Tony Kioko**
## Description
The Blog is a web application where you can create and share your opinions and other users can read and comment on them.

## User Stories
* As a user, I would like to view the blog posts submitted
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to alerted when a new post is made by joining a subscription.
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Create user account | **Click Sign Up button** | Form to capture user details|
| Welcome email | **On sign Up** | sends welcome email to new user|
| Display pitches | **On the Home page** | Pitches posted by users displayed per category |
| Post Pitch | **Login, Select category then Pitch** | Pitch created |
| Comment on Pitch | **Click comment on Pitch**  | Comment created for that specific pitch |
| Upvote or downvote | **click upvote/downvote**  | Pitch upvotes or downvotes increases  |


## Setup/Installation Requirements.
* Git clone https://github.com/TonyKioko/Pitches or download and unzip the repository from github.
* Have python3.6 installed in your machine
* Navigate into cloned file using the terminal.
* Run python3.6 -m venv --without-pip virtual to create a virtual environment.
* Run source virtual/bin/activate to activate the above created virtual environment.
* To run the app, type ./start.sh from your virtual environment on the terminal. In your favorite browser, open the link provided by the local host.

### Live Link ###
https://minpitch.herokuapp.com/

## Technologies used ##

* Python 3.6
* Flask
* Bootstrap

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs 
There are no known bugs.

<!-- ## Future additional features to be considered

* Store user credentials in a database.
* Use encryption algorithims to hash saved passwords. -->
 
### License
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)