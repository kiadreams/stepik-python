from datetime import datetime, timedelta


d = datetime.strptime(input(), '%d.%m.%Y').date()
d_end = datetime.strptime(input(), '%d.%m.%Y').date()
while not (d.day + d.month) % 2:
    d += timedelta(days=1)
while d <= d_end:
    if d.weekday() not in (0, 3):
        print(d.strftime('%d.%m.%Y'))
    d += timedelta(days=3)
