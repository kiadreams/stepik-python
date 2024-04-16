# !!! ВАЖНО Частые сценарии использования функции zip()!!!

# Сценарий 1. Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках.
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info, '\n')


# Сценарий 2. Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]

for x, y in zip(name, age):
    print(x, y)
print()


# !!!ВАЖНО-мы можем использовать одновременно функции zip() и enumerate()!!!:
list1 = ['a1', 'a2', 'a3']
list2 = ['b1', 'b2', 'b3']

for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(index, item1, item2)
print()

for elem in enumerate(zip(list1, list2)):
    print(elem)
print()
