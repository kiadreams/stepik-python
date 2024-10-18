from pprint import pprint
from itertools import zip_longest

a = [(1, 2), (3, 4), (5, 6)]
b = [x for t in a for x in t]
print(b)


# Функция zip без аргументов
print('Функция zip без аргументов'.center(100, '-'))

print(zip())
print(list(zip()))


# zip_longest из модуля itertools
print('zip_longest из модуля itertools'.center(100, '-'))
print('Обычный zip')
ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ('Australia', 'USA')
records = zip(ids, leaders, countries)
print(list(records))

print('zip_longest')
ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ('Australia', 'USA')
records = zip_longest(ids, leaders, countries)
print(list(records))
records_2 = zip_longest(ids, leaders, countries, fillvalue='Unknown')
print(list(records_2))



# Функция zip и неограниченное количество аргументов
print('Функция zip и неограниченное количество аргументов'.center(100, '-'))

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'
result_zip = zip(words, numbers, s)
pprint(list(result_zip))


# Распаковка значений при обходе объекта zip
print('Распаковка значений при обходе объекта zip'.center(100, '-'))

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'
for item in zip(words, numbers, s):
    print(item)


# Расцепление при помощи zip
print('Расцепление при помощи zip'.center(100, '-'))

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'
result_zip = zip(words, numbers, s)
print(list(zip(*result_zip)))
print()

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'
result_zip = zip(words, numbers, s)
col1, col2, col3 = zip(*result_zip)
print(col1)
print(col2)
print(col3)


# Разъединение (распаковка) двух или нескольких коллекций
print('Разъединение (распаковка) двух или нескольких коллекций'.center(100, '-'))
record = [(1, 'Elon Mask', 'Australia'),
          (2, 'Tim Cook', 'USA'),
          (3, 'Bill Gates', 'USA'),
          (4, 'Yang Zhou', 'China')]
ids, leaders, countries = zip(*record)
print(ids)
print(leaders)
print(countries)


# Итерация двух или нескольких коллекций
print('Итерация двух или нескольких коллекций (словарей)'.center(100, '-'))
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)


# Создание  и обновление словарей
print('Создание  и обновление словарей'.center(100, '-'))
employee_numbers = [2, 9, 18]
employee_names = ["Valentin", "Leonti", "Andrew"]

numbers = dict(zip(employee_numbers, employee_names))
employees = dict(zip(employee_names, employee_numbers))
print(numbers)
print('------')
print(employees)
# обновление словаря
other_num = [50, 63, 2]
other_names = ['Misha', 'Sergey', 'Ivan']
numbers.update(zip(other_num, other_names))
print('------')
print(numbers)


# Транспонирование матрицы
print('Транспонирование матрицы'.center(100, '-'))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
matrix_trans = [list(i) for i in zip(*matrix)]
print(matrix_trans)


# Параметр strict
print('Параметр strict'.center(100, '-'))

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300]
result_zip = zip(words, numbers, strict=True)
for word, num in result_zip:
  print(word, num)


