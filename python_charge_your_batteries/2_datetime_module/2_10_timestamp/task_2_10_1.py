from datetime import datetime, timezone


def from_timestamp_to_readable_date(unix_timestamp: int) -> str:
    pattern = '%d.%m.%Y %H:%M:%S'
    dt = datetime.fromtimestamp(unix_timestamp, timezone.utc)
    return dt.strftime(pattern)


from_timestamp_to_readable_date(0)
assert from_timestamp_to_readable_date(0) == '01.01.1970 00:00:00'
assert from_timestamp_to_readable_date(86400) == '02.01.1970 00:00:00'
assert from_timestamp_to_readable_date(312313922) == '24.11.1979 17:52:02'
assert from_timestamp_to_readable_date(4232313922) == '13.02.2104 02:45:22'
