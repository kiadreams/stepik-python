a, b = [int(s) for s in input().split()]
print([x**2 if a <= b else x**3 for x in range(*(a, b + 1) if a <= b else (a, b - 1, -1))])

# ВТОРОЙ ВАРИАНТ
print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)])
