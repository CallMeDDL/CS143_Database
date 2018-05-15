# CS143_Database
Database Systems (18 spring)
- Programming: PHP, MySQL, HTML, Python, Scala
- Framework: LAMP (Linux, Apache, MySQL, PHP)
- Tools: VirtualBox


## Project 1 A Moive Web Site
Build a Web site on movies, actors and their reviews, supported by a relational database system.
1. PHP web server warm-up  
Under our provided virtual machine setup, we created a simple PHP calculator application running inside the Apache server and accessible through a Web browser.
2. MySQL database  
Interacted with the MySQL database to create tables, populate the database using our movie and actor data, add "integrity constraints" that the database should satisfy, and run a few SELECT queries. And constructed a interface to connect PHP with MySQL, allowing a user to query the database through the website.
3. Movie database Web site  
Finally made user-friendly Web site of movie database (a la IMDB.com), adding Web pages and functionality that are needed for database interaction. Wrote PHP pages that execute various queries to find the information requested and to render the page in a user-friendly format.

## Project 2 Dashboard of Reddit data analysis
1. Text Parsing  
Wrote a function, preferably in Python to take horribly messy text from Reddit comments, and parse them into a smooth format that we can eventually use to train a classifier.
2. Transforming Data and Training Classifier  
Train a classifier using a Spark package called mllib.
3. Dashboard  
Created a dashboard with a few visualizations about sentiment has changed over time, over location, and other interesting findings.