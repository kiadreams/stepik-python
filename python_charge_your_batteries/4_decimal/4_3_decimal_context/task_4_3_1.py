from decimal import Decimal, getcontext


context = getcontext()
context.prec = 15
g = Decimal('9.81')
h = Decimal(input())
print((2 * h / g).sqrt())
