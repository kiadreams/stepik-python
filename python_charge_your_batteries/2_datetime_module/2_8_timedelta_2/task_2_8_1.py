from datetime import timedelta, date
from typing import Generator


def all_sundays(year: int) -> Generator[date, None, None]:
    day = date(year, 1, 1)
    period = timedelta(days=1)
    while day.isoweekday() != 7:
        day += period
    period = timedelta(weeks=1)
    while day.year == year:
        yield day
        day += period


for sunday in all_sundays(2023):
    print(sunday)