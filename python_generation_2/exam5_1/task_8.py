n = int(input())
result = [[abs(i - j) for j in range(n)] for i in range(n)]
for elem in result:
    print(*elem)