# CS143_Database
Database Systems (18 spring)
- Programming: PHP, MySQL, HTML, Python
- Framework: LAMP (Linux, Apache, MySQL, PHP)
- Tools: VirtualBox


## Project 1 A Moive Web Site
Built a Web site on movies, actors and their reviews, supported by a relational database system.
1. PHP web server warm-up  
- Under virtual machine, created a simple PHP calculator application running inside the Apache server and accessible through a Web browser.
2. MySQL database  
- Created tables, populated the database using movie and actor data interacting with the MySQL database
- Added integrity constraints that the database should satisfy.
- Constructed a interface to connect PHP with MySQL, allowing a user to query the database through the website.
3. Movie database Web site  
- Made user-friendly Web site of movie database (a la IMDB.com) based on LAMP stack and added Web pages and functionality that are needed for database interaction. 
- Wrote PHP pages that execute various queries to find the information requested and to render the page in a user-friendly format.

## Project 2 Dashboard of Reddit data analysis
1. Text Parsing  
- Wrote a function in Python to parse and clean horribly messy text from Reddit politics comments into a smooth format.
2. Transforming Data and Training Classifier  
- Transformed the comment data into unigrams, bigrams and trigrams features
- Trained a classifier to determine the sentiment toward Democrats and Republicans of a comment using a Spark package called mllib.