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

dbdata = {"symbol": "shibinr", "side": "buy", "type": "limit", "price": 100, "quantity": 1000, "recvWindow": 10000,
                "timestamp": int(time.time() * 1000)}

def coin_buy():
    api_key = "test_api_key"
    api_key = "fAitIbH2VIftuW34MC2hClQxukZ3hbUkhAuJTiW4II8PLSWXZilA0tRjgJSoXGsn"
    secret_key = "test_secret_key"
    secret_key = "3rApC1GeVeIZKEU0i5YmrazVUyoenxY3CWvpIE8J"
    client = Client(api_key=api_key, secret_key=secret_key)
    try:
        respi = client.send('create_test_order', dbdata)
        print(respi)

    except Exception as e:
        print(e)

coin_buy()
