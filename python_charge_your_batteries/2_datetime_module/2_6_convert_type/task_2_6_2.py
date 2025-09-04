from datetime import datetime
from typing import Optional


def convert_str_to_datetime(date_string: str, date_format: str) -> Optional[datetime]:
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError:
        return None

assert convert_str_to_datetime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p') == datetime(2014, 7, 1, 14, 43)
assert convert_str_to_datetime('2022-09-07 15:30:00', '%Y-%m-%d %H:%M:%S') == datetime(2022, 9, 7, 15, 30)
assert convert_str_to_datetime('Jul 1 2014 2:43PM', '%d %b %Y %I:%M%p') is None
assert convert_str_to_datetime('Invalid Date', '%d %b %Y %I:%M%p') is None
assert convert_str_to_datetime('29 July 2012', '%d %B %Y') == datetime(2012, 7, 29)
