from datetime import date


days = [0] * 7
for year in range(1, 10000):
    for month in range(1, 13):
        days[date(year, month, 13).weekday()] += 1
print(*days, sep='\n')
