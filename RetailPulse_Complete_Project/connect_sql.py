import pandas as pd
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',            # or your username
    password='jeeva',
    database='RetailPulseDB'
)

query = "SELECT * FROM transactions"
df = pd.read_sql(query, conn)
conn.close()
print(df.head())