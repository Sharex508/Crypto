
import requests
import websockets
from wazirx_sapi_client.rest import Client
from datetime import datetime as dt
import time
# import mysql.connector
# from mysql.connector import Error     
import json
import psycopg2
from psycopg2.extras import execute_values
import datetime
import time
import threading
import schedule



# import call
client = Client()
api_key = "test_api_key"
api_key = "fAitIbH2VIftuW34MC2hClQxukZ3hbUkhAuJTiW4II8PLSWXZilA0tRjgJSoXGsn"
secret_key = "test_secret_key"
secret_key = ""
client = Client(api_key=api_key, secret_key=secret_key)


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
        obj.update({"intialPrice": price, "hightPrice": price,
                   "margin": "", "purchasePrice": ""})

    # print ("done")
    return resp
    # return insert_data_db(resp)


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


def get_db_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="Twins@2018",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="wazirx")

    cursor = connection.cursor()
    return connection, cursor


def insert_data_db(resp):

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Twins@2018",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="wazirx")
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
        # INSERT INTO emp(id,emp_name)values(nextval('seq'),'Ron'); 1
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
        db_high_price = float(db_match_data[0]['highPrice'])
        # import pdb;pdb.set_trace()
        if api_last_price > db_high_price:
            # print (float(api_last_price),float(db_high_price))
            # margin =
            # (api_last_price-float(db_match_data[0]['intialPrice']))/float(db_match_data[0]['intialPrice'])*100
            margin = (
                api_last_price - float(db_match_data[0]['intialPrice'])) / api_last_price * 100
            update_record_profit(api_last_price, margin, ele)
            # print (margin)
            if float(margin) >= 3:
                print(margin)
                symbol = db_match_data[0]['symbol']
                balance = get_amount()
                # import pdb;pdb.set_trace()
                quantity = balance / float(api_last_price)
# data =  {"symbol": "btcinr", "side": "buy", "type": "limit", "price": float(api_last_price), "quantity":quantity , "recvWindow": 10000,
# "timestamp": int(time.time() * 1000)}
                data = {"symbol": ele, "side": "buy", "type": "limit", "price": float(api_last_price), "quantity": quantity, "recvWindow": 10000,
                      "timestamp": int(time.time() * 1000)}
                #coin_buy(data)
                msg = "{0} margin morethan {1}".format(symbol,margin)
                #mailSend(msg)

        else:
            margin = (api_last_price - float(db_match_data[0]['intialPrice'])) / float(
                db_match_data[0]['intialPrice']) * 100
            update_record_loss(api_last_price, margin, ele)


def update_record_profit(api_last_price, margin, ele):
    try:
        con = get_db_connection()
        sql = 'update trading_test set highPrice={0},lastPrice={1},margin={2} where symbol ={3}'.format(
            api_last_price, api_last_price, margin, repr(ele))
        con[1].execute(sql)
        con[0].commit()
    except Exception as e:
        print(e)
    finally:
        con[0].close()


def update_record_loss(api_last_price, margin, ele):
    try:
        con = get_db_connection()
        sql = 'update trading_test set lastPrice={0},margin={1} where symbol ={2}'.format(
            api_last_price, margin, repr(ele))
        con[1].execute(sql)
        con[0].commit()
    except Exception as e:
        print(e)
    finally:
        con[0].close()


def get_amount():
    try:
        con = get_db_connection()
        sql = "select balance from wallet"

        con[1].execute(sql)
        data = con[1].fetchone()
        print(data[0])
    except Exception as e:
        print(e)
    finally:
        con[0].close()
    return data[0]


def coin_buy(data):
    try:
        client.send('create_order', data)
        update_coin_record(data)
    except Exception as e:
        print(e)

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



def get_open_order_status():
    api_key = "test_api_key"
    api_key = "1Xdwd3vszGCIqQUrTOX2WPF6txeQg8pPb2Qkl5553XUuqEePJFOS2WDrxdpoFV3W"
    secret_key = "test_secret_key"
    secret_key = "5pG94NHjWycxA5ljZ2oNYcX08utpUT7xJothuNjd"
    client = Client(api_key=api_key, secret_key=secret_key)
    coin_names = get_buy_coins()
    if coin_names:
        for name in coin_names:
            resp = client.send('open_orders',
               {"symbol": name, "recvWindow": 10000,
                 "timestamp": int(time.time() * 1000)})
            if resp[1][0]['status'] == "success":
                try:
                    con=get_db_connection()
                    sql="UPDATE trading_test  SET status = 2 WHERE symbol={0}".format(
                        repr(name))
                    con[1].execute(sql)
                    sql2="select * from trading_test where symbol={0}".format(
                        repr(name))
                    con[1].execute(sql2)
                    data=con[1].fetchone()
                    now = dt.now()
                    time = now.strftime("%m/%d/%Y,%H:%M:%S")
                    if data:
                        sql3="INSERT into coin_buy (symbol,highPrice,lastPrice,purchasePrice,margin,sellMargin,created_at),\
                                values({0},{1},{2},{3},{4},{5},{6})".format(repr(data[0], data[2], data[2], data[2], "0", "0",repr(time)))

                        con[1].execute(sql3)
                        sql4 = ""
                        con[0].commit()
                except Exception as e:
                    print (e)
                finally:
                    con[0].close()

def get_buy_coins():
    names = []
    try:
        con = get_db_connection()
        sql = "SELECT symbol FROM trading_test WHERE status=1"
        con[1].execute(sql)
        rows = con[1].fetchall()
        for name in rows:
            names.append(name[0])
    except Exception as e:
            print (e)
    finally:
            con[0].close()
    return names
        
def get_coin_status():
    #import pdb;pdb.set_trace()
    try:
        con = get_db_connection()
        sql2 = "select * from trading_test where symbol={0}".format(repr('achinr'))
        con[1].execute(sql2)
        data = con[1].fetchone()
        if data:
            pass
    except Exception as e:
            print (e)
    finally:
            con[0].close()
get_coin_status()

def get_coin_buy_results():
    try:
        connection = psycopg2.connect(user="postgres",
                                          password="harsha508",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="crypto")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = "SELECT * FROM coin_buy"
        try:

            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            keys = ('symbol', 'highPrice',
                   'lastPrice', 'purchasePrice', 'margin','sellmargin')
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


def get_diff_of_coin_buy_db_api_values():
    start = time.time()
    db_resp = get_coin_buy_results()
    api_resp = get_data_from_wazirx()
    dicts_data = [obj['symbol'] for obj in db_resp]
    n = 25

    # using list comprehension
    final = [dicts_data[i * n:(i + 1) * n]
                               for i in range((len(dicts_data) + n - 1) // n)]
    # print (len(final))
    coin_task = threading.Thread(target=task_coin_buy, args=(db_resp, api_resp, final[0]))
    coin_task.start()
    coin_task.join()

def task_coin_buy(db_resp, api_resp, data, api_last_price, quantity):
    coin_task(db_resp, api_resp, data, api_last_price, quantity)
def coin_task(db_resp, api_resp, data, api_last_price , quantity):
    for ele in data:
        db_match_data = [item for item in db_resp if item["symbol"] == ele]
        api_match_data = [item for item in api_resp if item["symbol"] == ele]
        api_high_price = float(api_match_data[0]['highPrice'])
        db_high_price = float(db_match_data[0]['purchasePrice'])
        # import pdb;pdb.set_trace()
        if api_last_price > db_high_price:
            # print (float(api_last_price),float(db_high_price))
            # margin =
            # (api_last_price-float(db_match_data[0]['intialPrice']))/float(db_match_data[0]['intialPrice'])*100
            margin = (
                             api_high_price - float(db_match_data[0]['purchasePrice'])) / api_high_price * 100
            # print (margin)
            if float(margin) >= 3:
                print(margin)
                symbol = db_match_data[0]['symbol']
                # data =  {"symbol": "btcinr", "side": "sell", "type": "limit", "price": float(api_last_price), "quantity":quantity , "recvWindow": 10000,
                # "timestamp": int(time.time() * 1000)}
                data = {"symbol": ele, "side": "sell", "type": "limit", "price": float(api_high_price),
                        "quantity": quantity, "recvWindow": 10000,
                        "timestamp": int(time.time() * 1000)}
                coin_sell(data)


def coin_sell(data):
    try:
        client.send('create_order', data)
        update_coin_record(data)
    except Exception as e:
        print(e)

        
# get_open_order_status()
# get_data_from_wazirx()
# get_results()
# get_diff_of_db_api_values()
# get_amount()


import time

def show():
    get_diff_of_db_api_values()
    get_open_order_status()

    schedule.every(5).seconds.do(show)

    while 1:
        schedule.run_pending()
        time.sleep(1)
##

show()

