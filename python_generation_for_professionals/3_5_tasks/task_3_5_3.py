from datetime import datetime, date, time


schedule = {
    0: (time(9, 0, 0), time(21, 0, 0)),
    1: (time(10, 0, 0), time(18, 0, 0)),
}
cur_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
o_time, c_time = schedule[1] if cur_time.weekday() in (5, 6) else schedule[0]
if cur_time.time() < o_time or cur_time.time() >= c_time:
    print('Магазин не работает')
else:
    print(int((datetime.combine(cur_time.date(), c_time) - cur_time).total_seconds() // 60))

