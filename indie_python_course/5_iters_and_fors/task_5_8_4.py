n, m = map(int, input().split())
mtrx = [input() for _ in range(n)]
places = 0
for i in range(n):
    for j in range(m):
        if mtrx[i][j] == '.':
            neighbors = [
                mtrx[i][min(j + 1, m - 1)],
                mtrx[i][max(j - 1, 0)],
                mtrx[max(i - 1, 0)][j],
                mtrx[min(i + 1, n - 1)][j],
            ]
            if "*" not in neighbors:
                places += 1
print(places)
