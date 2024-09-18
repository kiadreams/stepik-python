n = int(input())
m = []
for _ in range(n):
    m.append([int(x) for x in input().split()])
d = [m[i][j] for i in range(n) for j in range(n) if i + j == n - 1]
print(d)