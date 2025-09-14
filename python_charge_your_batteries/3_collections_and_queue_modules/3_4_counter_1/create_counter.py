from collections import Counter

count_from_str = Counter('gallahad')  # создание Counter из строки
print(count_from_str)

words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']
names = Counter(words)

print(names)

count_from_dict = Counter({'red': 4, 'blue': 2})  # создание Counter из словаря
print(count_from_dict)

c = Counter(cats=4, dogs=8)  # создание Counter по ключевым аргументам
print(c)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
my_counter = Counter({key: value for key, value in my_dict.items()})
print(my_counter)
# Можно создать пустой счетчик и добавлять элементы по мере необходимости:
c_1 = Counter()
c_1.update([1, 2, 3, 3, 3, 4, 5, 5, 6])
print(c_1)
