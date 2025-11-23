from decimal import Decimal


# Создание Decimal из int
integer_num = 42
decimal_num = Decimal(integer_num)
print(decimal_num, type(decimal_num))
print()

# Создание Decimal из float
float_num = 3.14
decimal_num = Decimal(float_num)
print(decimal_num, type(decimal_num))
print()

print(Decimal(0.1))
print(Decimal(0.5))
print(Decimal(0.75))
"""
Обратите внимание, что преобразование числа float в Decimal может привести к
получению длинной последовательности цифр, как показано в примере выше. Это
связано с тем, что некоторые числа с плавающей запятой не могут быть точно
представлены в двоичном формате. Чтобы избежать этой проблемы, вы можете
создать экземпляр Decimal, используя строковое представление числа.
"""
# Создание Decimal из str
string_num = '3.14'
decimal_num = Decimal(string_num)
print(decimal_num, type(decimal_num))
print()

print(Decimal('0.1'))
print(Decimal('0.5'))
print(Decimal('0.75'))

# Создание Decimal из упорядоченной коллекции - кортежа или списка
tuple_num = (0, (3, 1, 4), -2)
decimal_num = Decimal(tuple_num)
print(decimal_num)
print()

print(Decimal((0, (3, 1, 1), -1)))
print(Decimal((1, (3, 1, 2), 0)))
print(Decimal((0, (3, 1, 3), 1)))
print(Decimal([1, (3, 1, 4), 2]))
print(Decimal([1, [0, 1, 5], 2]))
