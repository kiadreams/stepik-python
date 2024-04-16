from datetime import timedelta, datetime

watch_time = datetime.strptime(input(), '%H:%M:%S')
alarm_clock = watch_time + timedelta(seconds=int(input()))
print(alarm_clock.strftime('%H:%M:%S'))
