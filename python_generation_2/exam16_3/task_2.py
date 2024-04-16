from operator import mul
from functools import reduce


# Вариант 1
def product_of_odds_1(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result


# Вариант 2
def product_of_odds_2(data):
    return reduce(lambda a, n: a * n, filter(lambda x: x % 2 == 1, data), 1)


# Вариант 3
def product_of_odds_3(data):
    return reduce(lambda a, n: a * (n if n % 2 == 1 else 1), data, 1)


# Вариант 4
def product_of_odds_4(data):
    return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)



print(product_of_odds_1([1, 2, 4, 5, 6, 7]))
print(product_of_odds_2([1, 2, 4, 5, 6, 7]))
print(product_of_odds_3([1, 2, 4, 5, 6, 7]))
print(product_of_odds_4([1, 2, 4, 5, 6, 7]))
