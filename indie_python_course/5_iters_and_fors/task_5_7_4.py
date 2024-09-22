# Вывод элементов матрицы в порядке: справа на лево и сверху вниз

n, m = map(int, input().split())
mtrx = []
for i in range(n):
    mtrx.append([int(x) for x in input().split()][::-1])
[print(*x) for x in mtrx]