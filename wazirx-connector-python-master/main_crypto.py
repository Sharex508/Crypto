import requests
import websockets
from wazirx_sapi_client.rest import Client
from datetime import datetime as dt
import time
import mysql.connector
from mysql.connector import Error
import json
import psycopg2
##from psycopg2.extras import execute_values
import datetime
import time
import threading
import schedule

client = Client()
api_key = "test_api_key"
api_key = "fAitIbH2VIftuW34MC2hClQxukZ3hbUkhAuJTiW4II8PLSWXZilA0tRjgJSoXGsn"
secret_key = "test_secret_key"
secret_key = "3rApC1GeVeIZKEU0i5YmrazVUyoenxY3CWvpIE8J"
client = Client(api_key=api_key, secret_key=secret_key)

def get_data_from_wazirx():
    data = json.loads(requests.get(
        'https://api.wazirx.com/sapi/v1/tickers/24hr').text)
    print(data)
    return data

    
def get_results():
    try:
        connection = psycopg2.connect(user="postgres",
                                          password="Twins@2018",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="wazirx")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = "SELECT * FROM trading_test where status='0'"
        try:

            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            keys = ('symbol', 'intialPrice', 'highPrice',
                   'lastPrice', 'purchasePrice', 'margin')
            data = []
            for obj in results:
               data.append(dict(zip(keys, obj)))
            return data

        except Exception as e:
            print(e)
    except Exception as e:
            print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

