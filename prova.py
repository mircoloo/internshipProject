#!/usr/bin/python3
print("Content-Type: text/html\n\n")

import sys
sys.path.append("C:\\Users\\terresquall\\AppData\\Roaming\\Python\\Python39\\site-packages")

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
  user="root",
  password="",
  database="smishingDB"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM `twittdata`;")

print(cursor)