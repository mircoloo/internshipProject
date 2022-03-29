#!python3
import mysql.connector
import telGuard as tG

mydb = mysql.connector.connect(
  host="localhost",
  user="mirco",
  password="123",
  database="smishingDB"
)
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE smishingDB")
except:
    print('Database already exists')


#mycursor.execute("CREATE TABLE numeri (numer INT PRIMARY KEY, commento VARCHAR(255))")
sql = "INSERT INTO numeri VALUES ( %s , %s )"
"""
val = (1234, "insert da python")
mycursor.execute(sql, val)
mydb.commit()
response = mycursor.execute("SELECT * FROM numeri")
for x in response:
    print(x) """


df = tG.extract_data()
df_list = df.values.tolist()
values = [(el[0], el[1]) for el in df_list]
mycursor.executemany(sql, values)
mydb.commit()
print(mycursor.rowcount, "was inserted.") 
