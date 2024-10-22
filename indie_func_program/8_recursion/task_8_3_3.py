def gcd1(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd(a: int, b: int) -> int:
    if not b:
        return a
    return gcd(b, a % b)


print(gcd1(15, 5))
print(gcd(15, 5))