from decimal import localcontext, Decimal

x = Decimal('1.23456789')
y = Decimal('2.34567890')
print(x / y)  # Вне локального контекста
print()

with localcontext() as ctx:
    ctx.prec = 10
    print(x / y)  # Внутри локального контекста
    print(y / x)  # Внутри локального контекста
print()

print(y / x)  # Вне локального контекста