a, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(a)]

for i in range(a - 2, -1, -1):
    for j in range(b - 2, -1, -1):
        m[i][j] = m[i + 1][j] + m[i][j + 1]
for el in m:
    print(*el)