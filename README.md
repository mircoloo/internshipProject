# Introduction
This is the internship project 2021/2022, attended in Bruno Kessler Foundation, I carried out during my informatic engineering path in University of Trento.

## What is about?
This Smihing project is about building a framework can scrape some sites in order to retrieve usefull information about SMS phishing message, elaborate the datas and display them on a dashboard

## What is Smishing?
Smishing is the fraudulent practice of sending text messages purporting to be from reputable companies in order to induce individuals to reveal personal information, such as passwords or credit card numbers.
## Installation
In order to work, scripts need some requirments, there's a requirments.txt file in the project folder and where you are in the right path, just run the command:

```bash
pip install -r requirments.txt
```

We even need the driver for the browser scraping part (in this project i'm using Firefox as browser): https://github.com/mozilla/geckodriver/releases  here ther's a link where you can find the driver you need WORK IN PROGRESS...

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

The project is built using different technologies:
HTML, CSS, Javascript for the frontend aspect
PHP as backend languages
Python as Web information collector
mySQL as Database lanaguages

It is necessary, to see the dashboard online, host the project on a server. For the development I used XAMPP (here's the link: https://www.apachefriends.org/it/index.html)

On the sql_updater.py file, you can change the configuration in order to connect to the right database, in XAMPP, defualt values are (root as user, and no password, the hosting port is the http ones 80)
## Testing
After downloading the repository, put it on /htdocs/ folder, that are located dependetly on where you installed XAMPP, in defualt these should be the PATHS

LINUX: /opt/lampp/htdocs

  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
