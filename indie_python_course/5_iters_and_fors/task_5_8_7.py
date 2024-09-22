a, b = map(int, input().split())
m = [[0] * b for _ in range(a)]
k = iter(range(a * b))
for i in range(a):
    for j in (range(b - 1, -1, -1) if i % 2 else range(b)):
        m[i][j] = next(k)
for el in m:
    print(*el)