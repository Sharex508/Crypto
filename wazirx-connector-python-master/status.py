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
import schedule
from Buy import get_db_connection

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
                    sql4 = ""
                    con[0].commit()
                except Exception as e:
                    print (e)
                finally:
                    con[0].close()
            else:
                try:
                    con=get_db_connection()
                    sql1="UPDATE trading_test  SET retrycount = retrycount+1 WHERE symbol={0}".format(
                    repr(name))
                    con[1].execute(sql1)
                    sql4 = ""
                    con[0].commit()
                except Exception as e:
                    print (e)
                finally:
                    con[0].close()