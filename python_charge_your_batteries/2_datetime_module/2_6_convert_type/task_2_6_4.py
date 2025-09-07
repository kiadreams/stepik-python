import json
from datetime import datetime, time, date

dict_with_times = {
    'date': date(2023, 9, 2),
    'datetime': datetime(2023, 9, 2, 15, 30, 0),
    'time': time(15, 30, 19),
}


def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.strftime('Date registry: %d %B, %Y %H:%M')
    elif isinstance(obj, date):
        return obj.strftime('%d.%m.%Y')
    elif isinstance(obj, time):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


json_str = json.dumps(dict_with_times, default=json_serial)
assert json_str == '{"date": "02.09.2023", "datetime": "Date registry: 02 September, 2023 15:30", "time": "15:30:19"}'

print('Good')
