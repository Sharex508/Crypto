import psycopg2
from datetime import datetime as dt
from psycopg2 import Error

    


def data_from_wazirx(data):
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
                mailSend(msg)

        else:
            margin = (api_last_price - float(db_match_data[0]['intialPrice'])) / float(
                db_match_data[0]['intialPrice']) * 100
            update_record_loss(api_last_price, margin, ele)
