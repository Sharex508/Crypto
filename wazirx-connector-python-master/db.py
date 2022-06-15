import psycopg2
from datetime import datetime as dt
from psycopg2 import Error
from main_crypto import get_data_from_wazirx
import psycopg2
from psycopg2 import Error
import reset


def get_db_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="Twins@2018",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="wazirx")
                                  

    cursor = connection.cursor()

    return connection, cursor

def table_Create_crypto ():

    try:
        connection = psycopg2.connect(user="postgres",
                                            password="Harsha508",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="wazirx")

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
                symbol           TEXT    NOT NULL,
                intialPrice       TEXT,
                highPrice         TEXT,
                lastPrice         TEXT,
                purchasePrice     TEXT,
                margin            TEXT,
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


def data_ins_wazirx(data):
    try:
        connection = psycopg2.connect(user="postgres",
                                            password="Harsha508",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="wazirx")

        cursor = connection.cursor()
        now = dt.now()
        time = now.strftime("%m/%d/%Y,%H:%M:%S")
        # SQL query to create a new table
        sql1 = "insert into  coin_buy(symbol,highPrice,lastPrice,purchasePrice,margin,sellMargin,created_at)"
        sql2 = "values({0},{1},{2},{3},{4},{5},{6})".format(repr("chbinr"),repr("1234"),repr("1234"),repr("1234"),repr("1"),repr("1"),repr(time))
        sql3 = sql1+sql2
        print (sql3)
        cursor.execute(sql3)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()