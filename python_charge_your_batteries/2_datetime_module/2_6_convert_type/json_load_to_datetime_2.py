import json
from datetime import datetime


def convert_datetime_values(dct: dict):
    for key, value in dct.items():
        if key == 'date':
            dct[key] = datetime.strptime(dct['date'], '%d/%m/%Y').date()
        elif key == 'datetime':
            dct[key] = datetime.strptime(dct['datetime'], '%d.%m.%Y %H:%M:%S')
        elif key == 'time':
            dct[key] = datetime.strptime(dct['time'], '%H:%M:%S').time()
    return dct


json_str = '{"date": "02/09/2023", "datetime": "02.09.2023 15:30:00", "time": "15:30:19"}'

data = json.loads(json_str, object_hook=convert_datetime_values)
print(data)
print(type(data))
print()
print(data['date'], type(data['date']))
print(data['datetime'], type(data['datetime']))
print(data['time'], type(data['time']))