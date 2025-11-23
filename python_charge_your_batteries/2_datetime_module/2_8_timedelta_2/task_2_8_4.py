from datetime import datetime, timedelta


pattern = '%d-%m-%Y'
day = datetime.strptime(input(), pattern)
period = timedelta(days=28)
print('Payment Schedule:')
for i in range(1, 13):
    print(f'Payment {i}: {day.strftime(pattern)}')
    day += period
