from datetime import date


def get_day_of_year(dt: date) -> int:
    # Как вариант...
    print(dt.timetuple().tm_yday)
    return int(dt.strftime('%j'))


assert get_day_of_year(date(2023, 1, 3)) == 3
assert get_day_of_year(date(2023, 1, 8)) == 8
assert get_day_of_year(date(2023, 1, 31)) == 31
assert get_day_of_year(date(2023, 2, 28)) == 59
assert get_day_of_year(date(2024, 2, 28)) == 59
assert get_day_of_year(date(2023, 3, 1)) == 60
assert get_day_of_year(date(2020, 3, 1)) == 61
assert get_day_of_year(date(2023, 6, 15)) == 166
assert get_day_of_year(date(2000, 6, 15)) == 167
assert get_day_of_year(date(2023, 12, 31)) == 365
assert get_day_of_year(date(2004, 12, 31)) == 366
print('Good')
