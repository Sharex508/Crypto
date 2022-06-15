from datetime import datetime
import time
"""
d1 =  "2022-04-16 10:43:41"
now = datetime.fromisoformat(d1)
time_stamp= datetime.timestamp(now)
print (time_stamp)
"""



# current date and time
now1 = datetime.now()

timestamp1 = datetime.timestamp(now1)
print("timestamp =", timestamp1)



time.sleep(5)
now2 = datetime.now()

timestamp2 = datetime.timestamp(now2)
print("timestamp =", timestamp2)


diff = timestamp2-timestamp1
print (diff)