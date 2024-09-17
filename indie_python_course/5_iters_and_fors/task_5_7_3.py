# Вывод элементов матрицы в порядке: снизу вверх и справа на лево

m = []
for i in range(int(input())):
    m.append([int(x) for x in input().split()][::-1])
[print(*x) for x in zip(*m[::-1])]