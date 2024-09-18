a, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(a)]

for i in range(1, a):
    for j in range(1, b):
        m[i][j] = m[i - 1][j] + m[i][j - 1]
for el in m:
    print(*el)
