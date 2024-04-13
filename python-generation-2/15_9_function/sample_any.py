#  возвращает True, так как есть хотя бы один элемент, равный True
print(any([False, True, False]))
#  возвращает False, так как нет элементов, равных True
print(any([False, False, False]), '\n')

print(any([0, 0, 0]))
print(any([0, 1, 0]))
print(any([False, 0, 1]))
print(any(['', [], 'green']))
print(any({0j, 3+4j, 0.0}), '\n')


# При работе со словарями функция any() проверяет на соответствие True ключи словаря, а не их значения.
dict1 = {0: 'Zero'}
dict2 = {'Zero': 0, 'One': 1}

print(any(dict1))
print(any(dict2), '\n')


# !!! ВАЖНО - если переданный объект пуст, то функция any() возвращает значение False!!!
print(any([]))          #  передаем пустой список
print(any(()))          #  передаем пустой кортеж
print(any(''))          #  передаем пустую строку
print(any([[], []]))    #  передаем список, содержащий пустые списки



# !!!ВАЖНО!!! Реализация встроенной функции any() выглядит примерно так:
def any(iterable):
    for item in iterable:
        if item:
            return True
    return False