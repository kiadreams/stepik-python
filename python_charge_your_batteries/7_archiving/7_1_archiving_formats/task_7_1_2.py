# def decompress_string(compressed: str) -> str:
#     if not compressed or len(compressed) == 1:
#         return compressed
#     result, n = '', ''
#     for x in compressed:
#         if x.isalpha() and n:
#             result = result[0:-1] + result[-1] * int(n) + x
#             n = ''
#         elif x.isalpha():
#             result += x
#         else:
#             n += x
#     result = result[0:-1] + result[-1] * int(n) if n else result
#     return result.lower()


import re


def decompress_string(compressed: str) -> str:
    return re.sub(r'([a-z])(\d+)', lambda x: x[1]*int(x[2]), compressed).lower()


# Тестовые случаи
assert decompress_string("a4b3c1") == "aaaabbbc"
assert decompress_string("a1b5d1") == "abbbbbd"
assert decompress_string("w7") == "wwwwwww"
assert decompress_string("") == ""
assert decompress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
assert decompress_string("abcd") == "abcd"
assert decompress_string("xyz") == "xyz"

assert decompress_string("a6") == "aaaaaa"
assert decompress_string("a5") == "aaaaa"

assert decompress_string("AaBbCc") == "aabbcc"
assert decompress_string("a4b2c1a2") == "aaaabbcaa"
assert decompress_string("a4b3c2") == "aaaabbbcc"
assert decompress_string("a1000000") == "a" * 1000000
assert decompress_string("a1000000b500") == "a" * 1000000 + 'b' * 500
assert decompress_string("a1b1c1d1e1f1g1h1i1j1k1w10000") == "abcdefghijk" + "w" * 10000
