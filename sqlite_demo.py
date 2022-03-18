#!python3
import sqlite3
from telGuard import extractNumData


conn = sqlite3.connect('info.db')

#df = extractNumData(0)

#print(df)

c = conn.cursor()

#c.execute("DROP TABLE info")
#c.execute("""CREATE TABLE info(number INT PRIMARY KEY, comment text,type text, researchs int  )""")
#df.to_sql('info',conn, if_exists='replace', index = False)
#c.execute(f"INSERT INTO info VALUES ({}, 'Numero di Mirco', 'Numero serio', 17)")
#c.execute("INSERT INTO info VALUES (342343, 'Numero di sad', 'Numero non serio', 19)")
res = c.execute("SELECT * FROM info WHERE type = 'Sicuro'")
for r in res:
    print(r)

conn.commit()

conn.close()