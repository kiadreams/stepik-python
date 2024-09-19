n = int(input())
m = [[0] * n for _ in range(n)]
k = iter(range(1, n * n + 1))
for j1 in range(n):
    m[0][j1] = next(k)
step = 1
while step <= (n + 1) // 2:
    for down in range(n - (2 * step - 1)):
        m[step + down][n - step] = next(k)
    for left in range(n - (2 * step - 1)):
        m[n - step][(n - 1 - step) - left] = next(k)
    for up in range(n - 2 * step):
        m[(n - 1) - step - up][step - 1] = next(k)
    for right in range(n - 2 * step):
        m[step][step + right] = next(k)
    step += 1
for el in m:
    print(*el)