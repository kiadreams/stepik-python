from datetime import timedelta, date

day, month, year = map(int, input().split('.'))
curr_date, patern = date(year, month, day), '%d.%m.%Y'
for i in range(1, 11):
    print(curr_date.strftime(patern))
    curr_date += timedelta(days=i+1)
