from datetime import date


def saturdays_between_two_dates(start, end):
    saturdays = 0
    start_day, end_day = sorted([start.toordinal(), end.toordinal()])
    for some_day in range(start_day, end_day + 1):
        if date.fromordinal(some_day).isoweekday() == 6:
            saturdays += 1
    return saturdays

# d = 7
# some_date = date.fromordinal(d + 7)
# print(some_date)
# print(some_date.isoweekday())
# print()
# print(d % 7 or 7)


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))
