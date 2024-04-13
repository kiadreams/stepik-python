from datetime import datetime, timedelta

# Первый вариант
# tm = datetime.strptime(input(), '%H:%M:%S')
# diff_time = tm - datetime.strptime('00:00:00', '%H:%M:%S')
# print(int(diff_time.total_seconds()))

# Второй вариант
h, m, s = map(int, input().split(':'))
delta_time = timedelta(hours=h, minutes=m, seconds=s)
print(int(delta_time.total_seconds()))