from functools import reduce # type: ignore


# Для использования функции reduce() необходимо подключить специальный модуль functools. Функция reduce() имеет сигнатуру reduce(func, iterable, initializer=None). !!!! Если начальное значение не установлено, то в его качестве используется первое значение из последовательности iterable.!!!!

def func(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(func, numbers, 0)   # в качестве начального значения 0
print(total, '\n')

# в качестве начального значения взято numbers[0] - первое заначение последовательности!!! reduce(func, numbers)
total_2 = reduce(func, numbers)     # type: ignore
print(total_2)

# Функция reduce() во второй версии языка Python была встроенной, но в Python 3 ее решили перенести в модуль functools. Функция reduce() как и функции map() и filter() может принимать любой итерируемый объект.



# ПРИМЕР реализации функции reduce может выглядеть так:

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc
