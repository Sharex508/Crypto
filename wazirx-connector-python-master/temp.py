import psycopg2
from datetime import datetime as dt
from psycopg2 import Error
import psycopg2
from psycopg2 import Error
  
conn = psycopg2.connect(
   database="crypto", user='postgres', password='harsha508', host='database-1.cigflazwbdyg.ap-south-1.rds.amazonaws.com', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database  
#sql = '''CREATE database crypto''';

#Creating a database
#cursor.execute("DROP TABLE trading_test")
cursor.execute("DROP TABLE coin_buy")
print("Database deteted successfully........")

#Closing the connection
conn.close()
