import psycopg2
from datetime import datetime as dt
from psycopg2 import Error
import psycopg2
from psycopg2 import Error
  
conn = psycopg2.connect(
   database="crypto", user='postgres', password='harsha508', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database  
#sql = '''CREATE database crypto''';

#Creating a database
sql = "UPDATE trading_test SET  bp_margin='4' WHERE symbol='trxinr'"
cursor.execute(sql)
print("Database updated successfully........")

#Closing the connection
conn.close()