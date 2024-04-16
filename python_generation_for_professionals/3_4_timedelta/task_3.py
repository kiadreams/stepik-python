from datetime import datetime, timedelta

some_date = datetime.strptime(input(), '%d.%m.%Y')
period = timedelta(days=1)
yesterday, tommorow = some_date -  period, some_date + period
print(yesterday.strftime('%d.%m.%Y'), tommorow.strftime('%d.%m.%Y'), sep='\n')
