from datetime import date, timedelta


def count_work_days(start: date, end: date) -> int:
    start, end = (start, end) if start <= end else (end, start)
    period = timedelta(days=1)
    count = 0
    while start <= end:
        if start.isoweekday() not in (6, 7):
            count += 1
        start += period
    return count


# Проверка работы функции

start = date(2024, 3, 27)
end = date(2024, 3, 23)
print(count_work_days(start, end))


