
import requests
import websockets
from wazirx_sapi_client.rest import Client
import time
#import mysql.connector
#from mysql.connector import Error
import json
import psycopg2
from psycopg2.extras import execute_values
import datetime
import time
#import call


def get_data_from_wazirx():
    client = Client()

    api_key = "test_api_key"
    api_key = "fAitIbH2VIftuW34MC2hClQxukZ3hbUkhAuJTiW4II8PLSWXZilA0tRjgJSoXGsn"
    secret_key = "test_secret_key"
    secret_key = "3rApC1GeVeIZKEU0i5YmrazVUyoenxY3CWvpIE8J"
    client = Client(api_key=api_key, secret_key=secret_key)


    data = json.loads(requests.get('https://api.wazirx.com/sapi/v1/tickers/24hr').text)

    values = 'inr'

    resp = [d for d in data if d['quoteAsset']=="inr"]
    rem_list = ['baseAsset', 'quoteAsset', 'openPrice','lowPrice','highPrice','volume','bidPrice','askPrice','at']
    for obj in resp:
        for key in rem_list:
            obj.pop(key)
        price = obj['lastPrice']
        obj.update({"intialPrice":price,"hightPrice":price,"margin":"","purchasePrice":""})

    
    return resp
    #return insert_data_db(resp)


def get_results():
    try:
        connection = psycopg2.connect(user="postgres",
                                          password="Twins@2018",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="wazirx")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = "SELECT * FROM trading_test"
        try:
      
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            keys = ('symbol','intialPrice','highPrice',
                   'lastPrice','purchasePrice','margin')
            data =[]
            for obj in results:
               data.append(dict(zip(keys,obj)))
            return data
               
        except Exception as e:
            print (e)
    except Exception as e:
            print (e)
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
    return connection,cursor

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
        query = "INSERT INTO trading_test ({}) VALUES %s".format(','.join(columns))

        # convert projects values to sequence of seqeences
        values = [[value.strip() if type(value)=="str" else str(value)for value in obj.values()] for obj in resp]
        #import pdb;pdb.set_trace()
        tuples = [tuple(x) for x in values]
        #INSERT INTO emp(id,emp_name)values(nextval('seq'),'Ron'); 1
        cursor.executemany("INSERT INTO trading_test VALUES(%s,%s,%s,%s,%s,%s)", tuples)
        
 
        print("Data Inserted successfully in trading table.......... ")

    except Exception   as error:
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
    n = 30

    # using list comprehension
    final = [dicts_data[i * n:(i + 1) * n] for i in range((len(dicts_data) + n - 1) // n )]
    print (len(final))
    sys.exit(0)
    for ele in dicts_data:
        db_match_data  = [item for item in db_resp if item["symbol"] == ele]
        api_match_data  = [item for item in api_resp if item["symbol"] == ele]
        api_last_price = float(api_match_data[0]['lastPrice'])
        db_high_price =  float(db_match_data[0]['highPrice'])
        #import pdb;pdb.set_trace()
        if api_last_price > db_high_price:
            margin = (api_last_price-float(db_match_data[0]['intialPrice']))/float(db_match_data[0]['intialPrice'])*100
            update_record_profit(api_last_price,margin,ele)
        else:
            margin = (api_last_price-float(db_match_data[0]['intialPrice']))/float(db_match_data[0]['intialPrice'])*100
            update_record_loss(api_last_price,margin,ele)
    done = time.time()
    elapsed = done - start
    print(elapsed)
            
def update_record_profit(api_last_price,margin,ele):
    try:
        con = get_db_connection()
        sql='update trading_test set highPrice={0},lastPrice={1},margin={2} where symbol ={3}'.format(api_last_price,api_last_price,margin,repr(ele))
        con[1].execute(sql)
        con[0].commit()
    except Exception as e:
        print (error)
    finally:
        con[0].close()
        
def update_record_loss(api_last_price,margin,ele):
    try:
        con = get_db_connection()
        sql='update trading_test set lastPrice={0},margin={1} where symbol ={2}'.format(api_last_price,margin,repr(ele))
        con[1].execute(sql)
        con[0].commit()
    except Exception as e:
        print (error)
    finally:
        con[0].close()
    
            
            
        
        
        

#get_data_from_wazirx()
##get_results()
get_diff_of_db_api_values()




