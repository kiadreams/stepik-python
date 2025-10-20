from decimal import Decimal, getcontext, ROUND_UP

print(getcontext())

number = Decimal('475.456')

# Округляем до десятых с использованием ROUND_HALF_DOWN
print(number)
print()
print('Округляем до сотых')
print(number.quantize(Decimal('0.01')))  # Округляем до сотых
print(number.quantize(Decimal('1e-2')))  # Округляем до сотых
print('Округляем до десятых')
print(number.quantize(Decimal('0.1')))  # Округляем до десятых
print(number.quantize(Decimal('1e-1')))  # Округляем до десятых
print('Округляем до единиц методом ROUND_HALF_EVEN')
print(number.quantize(Decimal('1E0')))  # Округляем до единиц
print(number.quantize(Decimal('1e0')))  # Округляем до единиц
print('Округляем до единиц методом ROUND_UP')
print(number.quantize(Decimal('1E0'), rounding=ROUND_UP))  # Округляем до единиц
print(number.quantize(Decimal('1e0'), rounding=ROUND_UP))  # Округляем до единиц
print('Округляем до десятков')
print(number.quantize(Decimal('1E1')))  # Округляем до десятков
print(number.quantize(Decimal('1e1')))  # Округляем до десятков
print('Округляем до сотен')
print(number.quantize(Decimal('1E2')))  # Округляем до сотен
print(number.quantize(Decimal('1e2')))  # Округляем до сотен
