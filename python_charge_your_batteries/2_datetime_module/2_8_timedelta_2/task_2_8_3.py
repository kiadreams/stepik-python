from datetime import datetime, timedelta
import inspect


def date_range(start_date: datetime, end_date: datetime):
    period = timedelta(days=1)
    while start_date <= end_date:
        yield start_date
        start_date += period


# Проверки для функции-генератора date_range

assert inspect.isgeneratorfunction(date_range) is True, 'Нужно создать генератор-функцию'

print('print date interval from 1.1.2023 to 5.1.2023')
for date in date_range(datetime(2023, 1, 1), datetime(2023, 1, 5)):
    print(date.strftime('%d-%m-%Y'))
print('-'*10)
print('print date interval from 20.2.2000 to 2.3.2000')
for date in date_range(datetime(2000, 2, 20), datetime(2000, 3, 2)):
    print(date.strftime('%d-%m-%Y'))

assert len(list(date_range(datetime(2020, 2, 1), datetime(2020, 3, 1)))) == 30
assert len(list(date_range(datetime(2020, 5, 1), datetime(2020, 3, 1)))) == 0
assert len(list(list(date_range(datetime(2020, 5, 1), datetime(2024, 3, 1))))) == 1401