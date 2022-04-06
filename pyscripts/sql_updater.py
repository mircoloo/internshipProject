#!python3

import telGuarder as tG
import tellows
import mysql.connector
import twitt  

connection_config_dict = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'smishingDB',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }

""" mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smishingDB"
)    """

mydb = mysql.connector.connect(**connection_config_dict)

def update_tellows_data():
    mycursor = mydb.cursor()
    sql = "INSERT INTO teldata VALUES ( %s , %s , %s, %s, %s, %s)"  
    df = tellows.extract_data()
    df_list = df.values.tolist()
    values = [(el[0], el[1], el[2], el[3], el[4], el[5]) for el in df_list]
    mycursor.executemany(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.") 


def update_telguarder_data():
    mycursor = mydb.cursor()
    sql = "INSERT IGNORE teldata VALUES ( %s , %s , %s, %s, %s, %s)"  
    df = tG.extract_data()
    df_list = df.values.tolist()
    values = [(el[0], el[1], el[2], el[3], el[4], el[5]) for el in df_list]
    mycursor.executemany(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.") 

def update_twitter_data():
    mycursor = mydb.cursor()
    sql = "INSERT INTO twittdata VALUES ( %s , %s , %s, %s, %s, %s)"  
    df = twitt.extract_data()
    df_list = df.values.tolist()
    values = [(el[0], el[1], el[2], el[3], el[4], el[5]) for el in df_list]
    mycursor.executemany(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.") 


if __name__ == '__main__':
    update_telguarder_data()
    update_tellows_data()
    update_twitter_data()
