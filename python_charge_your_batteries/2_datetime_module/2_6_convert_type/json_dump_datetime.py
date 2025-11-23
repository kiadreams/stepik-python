import json
from datetime import datetime, time, date


class Cat:
    pass


cat = Cat()
print(cat)
dict_with_times = {
    'date': date(2023, 9, 2),
    'datetime': datetime(2023, 9, 2, 15, 30, 0),
    'time': time(15, 30, 19),
    'dt': 'd',
    'my_class': cat
}


def json_serial(obj):
    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    if isinstance(obj, Cat):
        return 'serialised the cat'
    raise TypeError("Type %s not serializable" % type(obj))


print(json.dumps(dict_with_times, default=json_serial))