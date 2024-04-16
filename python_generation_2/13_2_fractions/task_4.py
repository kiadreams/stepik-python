from fractions import Fraction as F


a, b = input(), input()
print(f'{a} + {b} = {F(a) + F(b)}')
print(f'{a} - {b} = {F(a) - F(b)}')
print(f'{a} * {b} = {F(a) * F(b)}')
print(f'{a} / {b} = {F(a) / F(b)}')