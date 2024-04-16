from datetime import datetime


dates = [datetime.strptime(date, '%d.%m.%Y')  for date in input().split()]
days = [abs((dates[i] - dates[i-1]).days) for i in range(1, len(dates))]
print(days)
