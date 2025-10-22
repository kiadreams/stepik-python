from datetime import datetime, timedelta


start = datetime(1, 1, 1, *map(int, input().split(':')))
end = datetime(1, 1, 1, *map(int, input().split(':')))
lesson, break_time = timedelta(minutes=45), timedelta(minutes=10)
while (start + lesson) <= end:
    print(start.strftime('%H:%M'), '-', (start + lesson).strftime('%H:%M'))
    start += lesson + break_time

