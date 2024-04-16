import json


def is_correct_json(string: str) -> bool:
    try:
        answer = json.loads(string)
        return True
    except json.JSONDecodeError:
        return False


s ='number = 17'

print(is_correct_json(s))

