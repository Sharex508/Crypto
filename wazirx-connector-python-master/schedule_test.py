import schedule
import time


def show():
    print ("sai")


schedule.every(2).seconds.do(show)

while 1:
    schedule.run_pending()
    #time.sleep(1)
    
