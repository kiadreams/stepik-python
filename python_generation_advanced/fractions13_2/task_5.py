from fractions import Fraction as F


n, result = int(input()), 0
for i in range(1, n + 1):
    result += F(1, i ** 2)
print(result)

# Второй вариант...
print(sum([F(1, num ** 2) for num in range(1, n + 1)]))
