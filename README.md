# Introduction
This is the internship project 2021/2022, attended in Bruno Kessler Foundation, I carried out during my informatic engineering path in University of Trento.

## What is the project about?
This Smihing project is about building a framework can scrape some sites in order to retrieve usefull information about SMS phishing message, elaborate the datas and display them on a dashboard

## What is Smishing?
Phishing is a type of Internet fraud that seeks to acquire a user’s credentials by deception. It includes theft of passwords, credit card numbers, bank account details and other confidential information.

Phishing messages usually take the form of fake notifications from banks, providers, e-pay systems and other organizations. The notification will try to encourage a recipient, for one reason or another, to urgently enter/update their personal data. Such excuses usually relate to loss of data, system breakdown, etc.

# Usage
## Install python libraries
The project is built using different technologies:
HTML, CSS, Javascript for the frontend aspect
PHP as backend languages
Python as Web information collector
mySQL as Database lanaguages

It is necessary, to see the dashboard online, host the project on a server. For the development I used XAMPP (here's the link: https://www.apachefriends.org/it/index.html)

In order to work, scripts need some requirments, there's a requirments.txt file in the project folder. When you are in the right path, just run the following command:

```bash
pip install -r requirments.txt
```
If you encount some errors, just try to install the libraries one at the time

## Install geckodriver of Firefox
We even need the driver for the browser scraping part (in this project i'm using Firefox as browser): https://github.com/mozilla/geckodriver/releases  here ther's a link where you can find the driver you need)





### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BEARER_TOKEN` with the bearer token generated after you created a twitter developer account: https://developer.twitter.com/en/portal/dashboard




## Running the server
After downloading the repository, put it on /htdocs/ folder, that are located dependetly on where you installed XAMPP, in defualt these should be the PATHS

MacOS: /Applications/XAMPP/htdocs

GNU LINUX: /opt/lampp/htdocs

Windows: C:\xampp\htdocs\ for standard installation

After that, run the XAMPP applications and start the Apache server and MYSQL database.
Default ports are 80 for Apache server and 3306 for the Database.

## Create the tables
Once the server is started, reach the "http://localhost:80" endpoint, open up the phpMyAdmin, and create a new Database, name it smishingDB, create new tables with the current sql querys:
```mySQL
CREATE TABLE teldata (number VARCHAR(30), comment TEXT, type VARCHAR(30), researchs INT, score INT, source VARCHAR(30));

CREATE TABLE twittdata (ID VARCHAR(30), comment TEXT, nickname VARCHAR(40), creation DATE, imageUrl TEXT, imageText TEXT, organization VARCHAR(30), link TEXT);
```

After you created the table, you can setup the script connect to the database

## Connect to the database

On the sql_updater.py file, you can change the configuration in order to connect to the right database, in XAMPP, defualt values are (root as user, and no password, the hosting port is the http ones 80)


```python
# ./pyscripts/sql_updater.py 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smishingDB"
)   


```

## Update the database

If all the stuff had been correctly setted up, in order to scrape the web and update your database, you just need to run the ```sql_updater.py``` script
inside the ```pyscripts``` folder.
On the console you can check some information like then number of rows interted

## Open the web Application

Now everything should be setted, the site is up! (locally), so search ```http://localhost/internshipProject``` on your browser

# The Web App

The web application is divided in three sections:
* Twitter cards
* Tellows and Telguarder tables
* Sospicious Links section

## Section one (Twitter)
On the section one, there are displayed in a form of cards, usefull information about recents twitts from the users about sms fraud, we can find:

* Creation date of the tweet
* (The name of organizations if present)
* The twitt comment
* (Sospicious link if present)
* The username of the poster
* (The image of the tweet if present)
  * If you hover the image, the text will be displayed

## Section two (Teldata)

On the section two, there are displayed  the datas reguarding the informations of recents number reports from the users. 

* Number
* Comment
* Type, is the category of the comment (for example fraud, telemarketing ecc.)
* Researchs
* Score
* Source
* Organizations

It is possible to filter the informations thanks to the use of the options menù

## Section three (Links)

On the section three, there are displayed  the datas reguarding the informations of sospicious links and the total number for each one



  

 





