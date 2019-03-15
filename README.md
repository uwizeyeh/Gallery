## PROJECT NAME
   ZOOM
## Description  

Zoom is a simple photo gallery web application to showcase beautiful pictures and designs. Users get to view photos updated by the site admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. The search functionality will search photos based on the categories.
## BDD

Simple photo gallery web application to showcase beautiful pictures and designs

 <!-- 
June 8th, 2018
By Richard Waweru
Description

Specifications
Get the specs here

Set Up and Installations
Prerequisites
Ubuntu Software
Python3.6
Postgres
python virtualenv
Clone the Repo
Run the following command on the terminal: git clone https://github.com/DevWaweru/Zoom.git && cd Zoom

Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database
psql
CREATE DATABASE zoom;
.env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'zoom'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3.6 manage.py makemigrations album
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

Known bugs
Copy functionality does not work

Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql
Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

License
Copyright (c) Richard Waweru --> -->