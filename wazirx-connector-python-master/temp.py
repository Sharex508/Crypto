import psycopg2
from datetime import datetime as dt
from psycopg2 import Error
from main_crypto import get_data_from_wazirx
import psycopg2
from psycopg2 import Error
import reset
  
#establishing the connection
conn = psycopg2.connect(
   user='postgres', password='Harsha508', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute(crypto)
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()