import sys
import json

# Вариант №1
# json_obj = []
# for l in sys.stdin:
#     if not l.strip():
#         break
#     json_obj.append(l.strip())
# data: dict = json.loads(sys.stdin.read())
# for key, value in data.items():
#     if isinstance(value, list):
#         value = ', '.join(map(str, value))
#     print(f'{key}: {value}')


# Вариант №2
data = json.loads(sys.stdin.read())

for key, value in data.items():
    if isinstance(value, list):
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')
