#!python3

from gc import collect
import pymongo
import telGuarder as tG
import tellows
import mysql.connector
import twitt  
import sys
import os


if __name__ == '__main__':

    client = pymongo.MongoClient("mongodb+srv://mirco:mircomirco@smishingdb.sf0xe.mongodb.net/?retryWrites=true&w=majority")
    db = client["test"]
    collection = db["teldata"]


    data = twitt.extract_data()

    collection.insert_one({"_id": 0, "prova": 1})

    print(db)
