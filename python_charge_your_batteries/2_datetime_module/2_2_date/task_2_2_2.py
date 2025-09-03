from datetime import date


def count_dates_within_interval(start_date: date,
                                end_date: date,
                                dates: list[date]) -> int:
    start_date, end_date = sorted([start_date, end_date])
    return len(list(filter(lambda x: start_date <= x <= end_date, dates)))


test_dates = [
    date(2021, 9, 1),
    date(2021, 9, 2),
    date(2021, 9, 3),
    date(2021, 9, 4),
    date(2021, 9, 5),
    date(2021, 9, 4),
    date(2021, 9, 3),
]
assert count_dates_within_interval(
    date(2021, 9, 1), date(2021, 9, 2), test_dates) == 2

assert count_dates_within_interval(
    date(2021, 9, 1), date(2021, 9, 3), test_dates) == 4

assert count_dates_within_interval(
    date(2021, 9, 3), date(2021, 9, 1), test_dates) == 4

assert count_dates_within_interval(
    date(2021, 9, 10), date(2021, 9, 6), test_dates) == 0

assert count_dates_within_interval(
    date(2021, 9, 10), date(2021, 9, 5), test_dates) == 1

assert count_dates_within_interval(
    date(2021, 8, 10), date(2021, 8, 20), test_dates) == 0

assert count_dates_within_interval(
    date(2021, 9, 20), date(2021, 8, 10), test_dates) == 7

print('Good')
