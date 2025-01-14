import math
from string import ascii_lowercase, digits


def get_primes():
    sieve = [True] * 10000
    for p in range(2, 10000):
        if sieve[p]:
            yield p
            for i in range(p * p, 10000, p):
                sieve[i] = False


g = get_primes()
print(*[next(g) for _ in range(20)])
print(ascii_lowercase+'.@_' + digits)
