import operator as op
# Чтобы не писать каждый раз функции, определяющие такие стандартные математические операции как сумма или произведение:

# def sum_func(a, b):
#     return a + b

# def mult_func(a, b):
#     return a * b

# можно использовать уже реализованные функции из модуля operator.

print(op.add(10, 20))  # сумма
print(op.floordiv(20, 3))  # целочисленное деление
print(op.neg(9))  # смена знака
print(op.lt(2, 3))  # проверка на неравенство <
print(op.lt(10, 8))  # проверка на неравенство <
print(op.eq(5, 5))  # проверка на равенство ==
print(op.eq(5, 9))  # проверка на равенство ==
print(op.mul(5, 9))  # произведение двух чисел

# !!! Модуль operator реализован на языке C, поэтому функции этого модуля работают в разы быстрее, чем самописные функции в Python. !!!


# !!! Если нам нужны строковые методы в виде функций, мы можем получить их через название типа str !!!