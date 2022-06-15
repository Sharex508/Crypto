import psycopg2
from datetime import datetime as dt
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Twins@2018",
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