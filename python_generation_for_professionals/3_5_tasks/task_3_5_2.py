from datetime import date, timedelta
from collections import Counter


days_of_week = Counter()
one_day = timedelta(days=1)
day = date(1, 1, 1)
end = date(9999, 12, 31)
while day < end:
    day += one_day
    if day.day == 13:
        days_of_week[day.isoweekday()] += 1
print(*[t[-1] for t in sorted(days_of_week.items())], sep='\n')
