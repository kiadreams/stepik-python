from fractions import Fraction as F


n = int(input())
values = [F(n - i, i) for i in range((n + 2) // 2, n)]
values = sorted([num for num in values if num.numerator + num.denominator == n])
print(values[-1])
