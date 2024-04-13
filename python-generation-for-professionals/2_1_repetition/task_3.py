# Вариант №1
# def is_valid(string: str) -> bool:
#     length_is_correct = bool(string) and len(string) in [4, 5, 6]
#     is_number = all(map(str.isdigit, string))
#     return length_is_correct and is_number


def is_valid(string: str) -> bool:
    return len(string) in (4, 5, 6) and string.isdigit()

print(is_valid('2314'))