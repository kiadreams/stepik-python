import json
from string import ascii_lowercase


alphabet = dict([(w, i + 1) for i, w in enumerate(ascii_lowercase)])
json_data = json.dumps(alphabet)
print(json_data)
