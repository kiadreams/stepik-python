from datetime import datetime, timezone
import pytz


def from_date_to_timestamp(date_string: str) -> float:
    # # 1 вариант реализации данного задания работает и здесь и на stepik
    dt = datetime.strptime(date_string, '%d %B %Y %H:%M:%S')
    dt_utc = dt.replace(tzinfo=timezone.utc)
    return dt_utc.timestamp()

    # # 2 вариант реализации данного задания работает и здесь и на stepik
    # parsed_date_string = datetime.strptime(date_string, '%d %B %Y %H:%M:%S')
    # tz = pytz.UTC
    # localized_date = tz.localize(parsed_date_string)
    # print(localized_date, localized_date.timestamp())
    # return localized_date.timestamp()


# print(datetime.fromtimestamp(1346502741.0))

assert from_date_to_timestamp("01 September 2012 12:32:21") == 1346502741.0
assert from_date_to_timestamp("19 August 2018 00:50:00") == 1534639800.0
assert from_date_to_timestamp("28 February 2012 16:00:00") == 1330444800.0
