# Вывод элементов матрицы в порядке: сверху вниз слева направо
m = []
for i in range(int(input())):
    m.append([int(x) for x in input().split()])
[print(*x) for x in zip(*m)]

