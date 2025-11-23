import json
from datetime import datetime, date, time


def convert_datetime_values(dct: dict):
    for key, value in dct.items():
        try:
            dct[key] = time.fromisoformat(value)
            continue
        except ValueError:
            pass
        try:
            dct[key] = date.fromisoformat(value)
            continue
        except ValueError:
            pass
        try:
            dct[key] = datetime.fromisoformat(value)
            continue
        except ValueError:
            pass
    return dct


def convert_datetime_values_2(dct):
    for key, value in dct.items():
        try:
            if 'T' in value:
                dct[key] = datetime.fromisoformat(value)
            elif '-' in value:
                dct[key] = date.fromisoformat(value)
            elif ':' in value:
                dct[key] = time.fromisoformat(value)
        except ValueError:
            pass
    return dct


json_str = '{"date": "2023-09-02", "datetime": "2023-09-02T15:30:00", "time": "15:30:19"}'
data = json.loads(json_str, object_hook=convert_datetime_values)
print(data)
print(type(data))
print(data['date'], type(data['date']))
print(data['datetime'], type(data['datetime']))
print(data['time'], type(data['time']))
print()

data_2 = json.loads(json_str, object_hook=convert_datetime_values_2)
print(data_2)
print(type(data_2))
print(data_2['date'], type(data_2['date']))
print(data_2['datetime'], type(data_2['datetime']))
print(data_2['time'], type(data_2['time']))