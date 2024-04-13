n, answer = int(input()), True
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            answer = False
print(["NO", "YES"][answer])
