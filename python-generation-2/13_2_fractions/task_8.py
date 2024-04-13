from fractions import Fraction as F


n = int(input())
values = {F(i, j) for j in range(1, n + 1) for i in range(1, j) if i}
print(*sorted(values), sep='\n')
