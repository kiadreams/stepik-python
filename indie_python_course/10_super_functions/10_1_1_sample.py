from random import randint
from typing import Generator

d = (randint(1, 20) for i in range(7))

# ГЕНЕРАТОР ПОДДЕРЖИВАЕТ

# print(sum(d))
# print(sorted(d))
# print(min(d))
# print(max(d))

# ГЕНЕРАТОРАЫ НЕ ПОДДЕРЖИВАЮТ
# print(reversed(d))
# print(len(d))


def gen_func():
    for i in [1, 2, 3]:
        yield i


f = gen_func()
print(f)

print(next(f))
print(next(f))
print(next(f))
# print(next(f))


def echo_round() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return "OK"


def infinite_sequence() -> Generator[int, None, None]:
    num = 0
    while True:
        yield num
        num += 1
