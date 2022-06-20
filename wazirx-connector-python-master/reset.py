from cgitb import text
import string
import psycopg2
from psycopg2 import Error
import requests
import websockets
import json
from wazirx_sapi_client.rest import Client
from main_crypto import get_data_from_wazirx
from psycopg2 import Error


def table_Create_crypto ():

    try:
        connection = psycopg2.connect(user="postgres",
                                            password="harsha508",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="crypto")

        cursor = connection.cursor()
        # SQL query to create a new table
        create_table_query = '''CREATE TABLE coin_buy
            (
            symbol           TEXT    NOT NULL,
            highPrice         TEXT,
            lastPrice         TEXT,
            purchasePrice     TEXT,
            margin            TEXT,
            sellMargin        TEXT,
            created_at TEXT,
            status TEXT
            ); '''
    ##    create_table_query = '''CREATE TABLE wallet
    ##        (
    ##            balance INT
    ##            );'''
        # Execute a command: this creates a new table
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL - coin_buy ")

        create_table_query = '''CREATE TABLE trading_test
                (
                symbol            TEXT    NOT NULL,
                intialPrice       TEXT,
                highPrice         TEXT,
                lastPrice         TEXT,
                bp_margin         TEXT,
                purchasePrice     TEXT,
                ap_margin         TEXT,
                sellMargin        TEXT,
                created_at        TEXT,
                retrycount        INteger,
                status            TEXT  DEFAULT 0
                ); '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL - trading_test ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_data_from_wazirx():
    client = Client()

    api_key = "test_api_key"
    api_key = "fAitIbH2VIftuW34MC2hClQxukZ3hbUkhAuJTiW4II8PLSWXZilA0tRjgJSoXGsn"
    secret_key = "test_secret_key"
    secret_key = "3rApC1GeVeIZKEU0i5YmrazVUyoenxY3CWvpIE8J"
    client = Client(api_key=api_key, secret_key=secret_key)

    data = json.loads(requests.get(
        'https://api.wazirx.com/sapi/v1/tickers/24hr').text)

    values = 'inr'

    resp = [d for d in data if d['quoteAsset'] == "inr"]
    rem_list = [
    'baseAsset',
    'quoteAsset',
    'openPrice',
    'lowPrice',
    'highPrice',
    'volume',
    'bidPrice',
    'askPrice',
     'at']
    for obj in resp:
        for key in rem_list:
            obj.pop(key)
        price = obj['lastPrice']
        marg=  float(price) + (float(price)/100)*3
        #mar = string(marg)
        obj.update({"intialPrice": price, "hightPrice": price,
                   "margin": marg, "purchasePrice": ""})

    print ("done")
    #return resp
    return insert_data_db(resp)
    

def insert_data_db(resp):

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="harsha508",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="crypto")
        connection.autocommit = True

        cursor = connection.cursor()
        columns = resp[0].keys()
        query = "INSERT INTO trading_test ({}) VALUES %s".format(
            ','.join(columns))

        # convert projects values to sequence of seqeences
        values = [[value.strip() if type(value) == "str" else str(value)
                               for value in obj.values()] for obj in resp]
        # import pdb;pdb.set_trace()
        tuples = [tuple(x) for x in values]
        cursor.executemany(
    "INSERT INTO trading_test VALUES(%s,%s,%s,%s,%s,%s)", tuples)
        print("Data Inserted successfully in trading table.......... ")

    except Exception as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

table_Create_crypto ()
get_data_from_wazirx()

