# def compress_string(string: str) -> str:
#     if not string or len(string) == 1:
#         return string
#     result = ''
#     curr_l = string[0].lower()
#     count = 1
#     for l in string[1:].lower():
#         if l == curr_l:
#             count += 1
#         else:
#             result += f'{curr_l}{count}'
#             curr_l = l
#             count = 1
#     result += f'{curr_l}{count}'
#     return result if len(result) < len(string) else string

from itertools import groupby


def compress_string(string: str) -> str:
    result = ''.join(f'{k}{len(list(g))}' for k, g in groupby(string.lower()))
    return result if len(result) < len(string) else string


# Тестовые случаи с корректными входными данными
assert compress_string("aaaabbbc") == "a4b3c1"
assert compress_string("abbbbbd") == "a1b5d1"
assert compress_string("wwwwwww") == "w7"
assert compress_string("") == ""


# Тестовые случаи с входными данными, которые не нуждаются в сжатии
assert compress_string("abcd") == "abcd"
assert compress_string("xyz") == "xyz"
assert compress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"

# Тестовые случаи с регистронезависимостью
assert compress_string("aaAAaa") == "a6"
assert compress_string("aAaAA") == "a5"
assert compress_string("AaBbCc") == "AaBbCc"
assert compress_string("aaaAbbCaa") == "a4b2c1a2"
assert compress_string("AAAABBBCC") == "a4b3c2"

# Тестовые случаи с длинной строки
assert compress_string("a" * 1000000) == "a1000000"
assert compress_string("a" * 1000000 + 'b' * 500) == "a1000000b500"
assert compress_string("abcdefghijk" + "w" * 10000) == "a1b1c1d1e1f1g1h1i1j1k1w10000"