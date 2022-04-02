#!python3
import mysql.connector
import telGuard as tG
import tellows
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smishingDB"
)   


def update_tellows_data():
    mycursor = mydb.cursor()
    sql = "INSERT IGNORE tellows VALUES ( %s , %s , %s, %s)"  
    df = tellows.extract_data()
    df_list = df.values.tolist()
    values = [(el[0], el[1], el[2], el[3]) for el in df_list]
    mycursor.executemany(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.") 


def update_telguard_data():
    mycursor = mydb.cursor()
    sql = "INSERT IGNORE telguard VALUES ( %s , %s , %s, %s)"  
    df = tG.extract_data()
    df_list = df.values.tolist()
    values = [(el[0], el[1], el[2], el[3]) for el in df_list]
    mycursor.executemany(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.") 

if __name__ == '__main__':
    update_telguard_data()
