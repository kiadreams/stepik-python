from datetime import datetime, date
import time


# timestamp
today = date.fromtimestamp(time.time())
now = datetime.fromtimestamp(time.time())

print('Date is:', today)
print('Time and date is:', now)