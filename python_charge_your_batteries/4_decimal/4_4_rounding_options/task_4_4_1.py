from decimal import Decimal, ROUND_UP


amount, percent, years = map(Decimal, [input() for _ in range(3)])
total = amount * (1 + percent / 100) ** years
print(total.quantize(Decimal('1.0000'), rounding=ROUND_UP))
