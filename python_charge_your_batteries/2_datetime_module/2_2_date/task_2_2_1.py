from datetime import date
from typing import Optional


def find_max_date(dates: list[date]) -> Optional[date]:
    return max(dates, default=None)


assert find_max_date([]) is None

assert find_max_date([date(2022, 10, 10)]) == date(2022, 10, 10)

assert find_max_date([
    date(2022, 10, 10),
    date(2021, 12, 31),
    date(2023, 1, 1)
]) == date(2023, 1, 1), "Should return the latest date in the list"

assert find_max_date([
    date(2022, 10, 10),
    date(2022, 10, 10),
    date(2021, 12, 31)
]) == date(2022, 10, 10)

assert find_max_date(
    [date(2007, 11, 24), date(2018, 5, 7), date(2019, 6, 3),
     date(2016, 9, 7), date(2021, 4, 3), date(2019, 3, 11),
     date(2002, 8, 19), date(2020, 7, 8), date(2007, 6, 19),
     date(2006, 9, 19), date(2015, 7, 6), date(2013, 5, 1),
     date(2014, 2, 16), date(2005, 1, 9), date(2001, 10, 28),
     date(2002, 12, 20), date(2002, 3, 17), date(2009, 10, 28),
     date(2016, 8, 27), date(2000, 1, 24), date(2005, 8, 25),
     date(2000, 9, 20), date(2001, 12, 5), date(2003, 10, 16),
     date(2012, 9, 11), date(2010, 10, 15), date(2002, 2, 15),
     date(2018, 6, 10), date(2005, 11, 23), date(2007, 8, 19)]) == date(2021, 4, 3)

print('Good')