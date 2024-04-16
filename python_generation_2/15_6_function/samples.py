from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence',
         ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

# смена знаков элементов списка
opposite_numbers = list(map(operator.neg, numbers))
concat_words = reduce(operator.add, words)  # конкатенация элементов списка

print(opposite_numbers)
print(concat_words)

print()

pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']

uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))

print(uppered_pets)
print(capitalized_pets)
print(only_letters)

print()

my_list = list('asdfgh')
print(my_list)
result = map(str.upper, my_list) # map возвращает итератор
print(result)               # Выводит объект итератора
print(list(result)) # !!!Преобразует итератор в список, ОПУСТОШАЯ ЕГО!!!
print(*result)      # Итератор пуст, поэтому ничего не распокуется!!!
print(list(result)) # В список ничего не преобразуется - ИТЕРАТОР ПУСТ!!!

# Итераторы — это такие штуки, которые, очевидно, можно итерировать :)
# Получить итератор мы можем из любого итерируемого объекта.
# Для этого нужно передать итерируемый объект во встроенную функцию iter
# После того, как мы получили итератор, мы можем передать его встроенной функции next

my_iter = iter(map(str.capitalize, my_list))
print(next(my_iter))
print(next(my_iter))
print(list(my_iter))
print(list(my_iter))

print()

# !!!БОМБА!!! Объединение элементов списка в список со всеми элементами!!!
result_5 = sum([['a', 'b'], ['x', 'c'], ['f', 'd']], [])
print(result_5)
# print(sum(['a', 'd'], start='b')) # Объединение строк не работает!!!
