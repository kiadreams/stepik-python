# Вывод элементов матрицы в порядке: слева направо снизу вверх

n, m = map(int, input().split())
mtrx = []
for i in range(n):
    mtrx.append([int(x) for x in input().split()])
[print(*x) for x in mtrx[::-1]]
