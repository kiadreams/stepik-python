def quick_power(a, n):
    print(f'State: {a=}, {n=}')
    if n == 0:
        return 1
    if n % 2:
        return a * quick_power(a, n - 1)
    return quick_power(a, n // 2) ** 2


print(quick_power(3, 4))