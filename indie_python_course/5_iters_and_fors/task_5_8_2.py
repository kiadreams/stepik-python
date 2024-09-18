n = int(input())
a, b, c = map(int, input().split())
m = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            m[i][j] = a
        elif i > j:
            m[i][j] = b
        else:
            m[i][j] = c
for el in m:
    print(*el)
