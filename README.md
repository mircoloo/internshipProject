# Introduction
This is the internship project 2021/2022, attended in Bruno Kessler Foundation, I carried out during my informatic engineering path in University of Trento.

## What is the projet about?
This Smihing project is about building a framework can scrape some sites in order to retrieve usefull information about SMS phishing message, elaborate the datas and display them on a dashboard

## What is Smishing?
Smishing is the fraudulent practice of sending text messages purporting to be from reputable companies in order to induce individuals to reveal personal information, such as passwords or credit card numbers.

## Installation
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

We even need the driver for the browser scraping part (in this project i'm using Firefox as browser): https://github.com/mozilla/geckodriver/releases  here ther's a link where you can find the driver you need)


## Usage




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


### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BEARER_TOKEN` with the bearer token generated after you created a twitter developer account: https://developer.twitter.com/en/portal/dashboard




## Testing
After downloading the repository, put it on /htdocs/ folder, that are located dependetly on where you installed XAMPP, in defualt these should be the PATHS

MacOS: /Applications/XAMPP/htdocs

GNU LINUX: /opt/lampp/htdocs

