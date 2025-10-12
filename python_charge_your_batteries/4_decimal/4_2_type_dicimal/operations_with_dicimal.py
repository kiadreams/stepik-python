from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.2')

a = Decimal(1.5)
b = Decimal(2.5)

print(x, '....', y, '....', x + y, '....', y / x)
print(a, '....', b, '....', a + b, '....', a * b)
print()

num_constructor = [0, (9, 1, 0, 2), 2]
num_decimal = Decimal(num_constructor)
print(num_decimal)
