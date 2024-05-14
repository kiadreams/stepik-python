# Встроенная функция zip() объединяет отдельные элементы из каждой переданной ей последовательности (итерируемого объекта) в кортежи.
# Сигнатура функции следующая: zip(*iterables). В качестве iterable может выступать любой итерируемый объект:
#  - список;
#  - кортеж;
#  - строка;
#  - множество;
#  - словарь и т.д.

numbers = [1, 2, 3]
words = ['one', 'two', 'three']

for pair in zip(numbers, words):
    print(pair)
print()

numbers = [1, 2, 3]
words = ['one', 'two', 'three']

result = zip(numbers, words)

print(result)
print(list(result), '\n')


# Мы можем передавать функции zip() сколько угодно итерируемых объектов.
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result), '\n')


# Мы можем передать функции zip() даже один итерируемый объект.
numbers = [1, 2, 3, 4]
result = zip(numbers)
print(list(result), '\n')


# Если функции zip() передать итерируемые объекты, имеющие разную длину, то объект с наименьшим количеством элементов определяет итоговую длину.
numbers = [1, 2, 3, 4]
words = ['one', 'two']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result), '\n')
