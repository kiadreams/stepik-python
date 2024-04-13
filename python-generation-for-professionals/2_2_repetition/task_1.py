ways = [int(input()) for _ in range(3)]
a, b, c = sorted(ways)
x1, x2 = (a + b) * 2, a + b + c
print(x1 if x1 < x2 else x2)
