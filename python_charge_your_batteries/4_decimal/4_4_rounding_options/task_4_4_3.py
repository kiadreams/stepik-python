from decimal import Decimal


p, v, n = map(Decimal, [input() for _ in range(3)])
r = Decimal('8.314462618')
t = p * v / n / r
print(t.quantize(Decimal('1e-10'), 'ROUND_HALF_DOWN'))
