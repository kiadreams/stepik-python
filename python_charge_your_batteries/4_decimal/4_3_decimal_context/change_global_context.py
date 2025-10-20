from decimal import (
    Decimal,
    Context,
    setcontext,
    ExtendedContext,
    ROUND_HALF_DOWN,
    getcontext,
    BasicContext,
)

print("Current context", getcontext())
print(Decimal(1) / Decimal(6))
print()

my_context = Context(prec=60, rounding=ROUND_HALF_DOWN)
setcontext(my_context)
print("Current context", getcontext())
print(Decimal(1) / Decimal(7))
print()

setcontext(ExtendedContext)
print("Current context", getcontext())
print(Decimal(1) / Decimal(7))
print(Decimal(42) / Decimal(0))  # Не происходит исключения при делении на ноль
print()

setcontext(BasicContext)
print('Current context', getcontext())
print(Decimal(42) / Decimal(0))  # Произойдет исключение
