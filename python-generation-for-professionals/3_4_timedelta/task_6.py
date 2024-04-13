from datetime import date, timedelta

def num_of_sundays(year: int) -> int:
    count_sundays = 0
    start = date(year=year, month=1, day=1)
    while start.year == year:
        if start.weekday() == 6:
            count_sundays += 1
        start += timedelta(days=1)
    return count_sundays

print(num_of_sundays(2020))