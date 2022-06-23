from tokenize import Double
import requests
import websockets
from wazirx_sapi_client.rest import Client
from datetime import datetime as dt
import time    
import json
import psycopg2
from psycopg2.extras import execute_values
import datetime
import time
import threading
import schedule
from notifications import notisend
client = Client()
import re
import pandas as pd



def get_db_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="harsha508",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="crypto")

    cursor = connection.cursor()
    return connection, cursor

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
        marg = float(price) + (float(price)/100)*3
        obj.update({"intialPrice": price, "hightPrice": price,
                   "bp_margin": marg, "purchasePrice": ""})

    # print ("done")
    return resp
    # return insert_data_db(resp)


def get_results():
    try:
        connection = psycopg2.connect(user="postgres",
                                          password="harsha508",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="crypto")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = "SELECT symbol, intialPrice, highPrice, lastPrice, purchasePrice, bp_margin FROM trading_test where status='0'"
        try:

            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            keys = ('symbol', 'intialPrice', 'highPrice',
                   'lastPrice', 'purchasePrice', 'bp_margin')
            data = []
            for obj in results:
               data.append(dict(zip(keys, obj)))
        
            #print(pd.DataFrame(data))
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

            
def get_diff_of_db_api_values():
    start = time.time()
    db_resp = get_results()
    api_resp = get_data_from_wazirx()
    dicts_data = [obj['symbol'] for obj in db_resp]
    n = 25

    # using list comprehension
    final = [dicts_data[i * n:(i + 1) * n]
                               for i in range((len(dicts_data) + n - 1) // n)]
    # print (len(final))
    t1 = threading.Thread(target=task1, args=(db_resp, api_resp, final[0]))
    t2 = threading.Thread(target=task2, args=(db_resp, api_resp, final[1]))
    t3 = threading.Thread(target=task3, args=(db_resp, api_resp, final[2]))
    t4 = threading.Thread(target=task4, args=(db_resp, api_resp, final[3]))
    t5 = threading.Thread(target=task5, args=(db_resp, api_resp, final[4]))
    t6 = threading.Thread(target=task6, args=(db_resp, api_resp, final[5]))

    # starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    done = time.time()
    elapsed = done - start
    print(elapsed)


def task1(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task2(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task3(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task4(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task5(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task6(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task7(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task8(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task9(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task10(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task11(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task12(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task13(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task14(db_resp, api_resp, data):
    task(db_resp, api_resp, data)


def task(db_resp, api_resp, data):
    for ele in data:
        db_match_data = [item for item in db_resp if item["symbol"] == ele]
        api_match_data = [item for item in api_resp if item["symbol"] == ele]
        api_last_price = float(api_match_data[0]['lastPrice'])
        print(api_last_price)
        print(db_match_data[0])
        db_margin = float(db_match_data[0]['bp_margin'])
        initialp =  float(db_match_data[0]['intialPrice'])

        print(db_margin)

    if api_last_price >= db_margin:
        print(db_margin) 
        symbol = db_match_data[0]['symbol']
                #balance = get_amount()
        quantity = 100 / float(api_last_price)
        data1 = {"symbol": ele, "side": "buy", "type": "limit", "initial price": initialp, "purchasing price": float(api_last_price), "dbmargin":db_margin, "quantity": quantity, }
        data = {"symbol": ele, "side": "buy", "type": "limit", "price": float(api_last_price), "quantity": quantity, "recvWindow": 10000,
                "timestamp": int(time.time() * 1000)}
        msg = data1
        notisend(msg)

def coin_buy(data):
    try:
        client.send('create_order', data)
        update_coin_record(data)
    except Exception as e:
        print(e)
        notisend(e)

def update_coin_record(info):
    try:
        con = get_db_connection()
        sql= "UPDATE trading_test  SET status = 1 ,purchasePrice= {1}WHERE symbol={0}".format(repr(info['symbol'], info['price']),);
        con[1].execute(sql)
        con[0].commit()
    except Exception as e:
        print(e)
    finally:
        con[0].close()

#get_diff_of_db_api_values()
#get_open_order_status()
