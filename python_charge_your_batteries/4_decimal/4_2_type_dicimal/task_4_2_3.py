from decimal import Decimal


rate, amount = [Decimal(input()) for _ in range(2)]
print(rate * amount)
