from datetime import datetime, date, time, timedelta

current_dt = datetime.now()
my_dt = datetime(year=2020, month=3, day=21, hour=12, minute=30)
diff = current_dt - my_dt

print(diff, type(diff))
print()

current_date = date.today()
my_date = date(2000, 12, 31)
diff_2 = current_date - my_date

print(diff_2, type(diff_2))
print()

current_time = datetime.now().time()
my_time = time(hour=12, minute=30)

# !!! со временем так не работает...
# print(current_time - my_time)

print(current_dt - datetime.combine(my_date, time()))
print(current_dt.date() - my_date)
print(current_dt, current_dt - timedelta(days=1, hours=1))
print()

first_dt = datetime(2012, 9, 28, 12, 32, 30)
second_dt = datetime(2024, 5, 5, 8)

print((first_dt - second_dt).total_seconds())



