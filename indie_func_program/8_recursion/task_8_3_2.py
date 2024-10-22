def power(a: int, n: int) -> int:
    if not n:
        return 1
    return a * power(a, n - 1)


print(power(2, 5))