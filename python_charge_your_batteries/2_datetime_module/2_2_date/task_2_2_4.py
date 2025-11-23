from datetime import date


def add_years(dt: date, years: int) -> date:
    try:
        new_date = dt.replace(year=dt.year + years)
    except ValueError:
        new_date = dt.replace(year=dt.year + years, month=dt.month + 1, day=1)
    return new_date


assert add_years(date(2023, 1, 1), -1) == date(2022, 1, 1)
assert add_years(date(2023, 1, 1), 0) == date(2023, 1, 1)
assert add_years(date(2023, 1, 1), 2) == date(2025, 1, 1)
assert add_years(date(2023, 1, 1), 10) == date(2033, 1, 1)
assert add_years(date(2000, 2, 29), 1) == date(2001, 3, 1)
assert add_years(date(2020, 2, 29), 20) == date(2040, 2, 29)
print('Good')