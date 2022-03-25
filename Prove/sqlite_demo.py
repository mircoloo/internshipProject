#!python3
import sqlite3
from telGuard import extract_data


conn = sqlite3.connect('info.db')

#df = extractNumData(0)

def search_num_information(num: int):
    res = c.execute(f"SELECT * FROM info WHERE number = {num}")

    return res.fetchone() if res != None else "number not in database"

#df = extract_data(0)


#print(df)

c = conn.cursor()

#c.execute("DROP TABLE info")
#c.execute("""CREATE TABLE info(number INT PRIMARY KEY, comment text,type text, researchs int  )""")
#df.to_sql('info',conn, if_exists='append', index = False)
#c.execute(f"INSERT INTO info VALUES ({}, 'Numero di Mirco', 'Numero serio', 17)")
#c.execute("INSERT INTO info VALUES (342343, 'Numero di sad', 'Numero non serio', 19)")
res = c.execute("SELECT * FROM info")
for r in res:
    print(r)
#print(search_num_information('0230300659'))

conn.commit()

conn.close()