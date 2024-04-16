from fractions import Fraction as F
from math import factorial


n = int(input())
print(sum([F(1, factorial(num)) for num in range(1, n + 1)]))

# Второй вариант...
every_fac, result = 1, 0
for i in range(1, n + 1):
    every_fac *= i
    result += F(1, every_fac)
print(result)