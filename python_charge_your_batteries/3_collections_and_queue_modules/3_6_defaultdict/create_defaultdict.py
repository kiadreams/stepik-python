from collections import defaultdict

# создание defaultdict, использующего int() в качестве значения по умолчанию
count = defaultdict(int)

# добавление элементов в словарь
count['a'] = 1
count['b'] = 2

# обращение к несуществующему ключу
print(count['c'])  # выведет 0, так как int() возвращает 0

print(count)

# обращение к несуществующему ключу d,
# получаем значение по умолчанию и сразу увеличиваем его на 5
count['d'] += 5

print(count)
print()

#  создание defaultdict, использующего list() в качестве значения по умолчанию
marks = defaultdict(list)

# добавление элементов в словарь
marks['Ben'].append(5)
marks['Asya'].append(4)

# обращение к несуществующему ключу
print(marks['Kate'])  # выведет [], так как list() возвращает []

print(marks)

# обращаясь к несуществующему ключу John,
# получаем значение по умолчанию и сразу расширяем его на списком [4, 5, 5, 4]
marks['John'].extend([4, 5, 5, 4])

print(marks)
print()

#  создание defaultdict, использующего list() в качестве значения по умолчанию
marks = defaultdict(list)

# но не смотря на тип list, мы создаем значения другого типа
marks['Ben'] = 'Harrison'
marks['Asya'] = (4, 5, 6, 9)
marks['Kate'] = False

# Обращение к несуществующему ключу создаст пару с дефолтным значением
marks['Julia']

marks['Boris'].append('Hello')
print(marks)
print()