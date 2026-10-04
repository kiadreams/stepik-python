import calendar as cl
from datetime import datetime

date = datetime.strptime('2008 1', '%Y %m')
print(cl.monthrange(date.year, date.month)[1])




