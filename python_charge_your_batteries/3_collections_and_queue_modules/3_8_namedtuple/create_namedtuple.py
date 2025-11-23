from collections import namedtuple

Person = namedtuple('Person', 'name birth_date country')

person = Person('Megan Jones', '1987-07-16', 'Bolivia')

print(person.name)  # Выводит: 'Megan Jones'
print(person.birth_date)  # Выводит: 1987-07-16
print(person.country)  # Выводит: Bolivia

print(person[0])  # Выводит: 'Megan Jones'
print(person[1])  # Выводит: 1987-07-16
print(person[2])  # Выводит: Bolivia
print()


# Пример с указанием полей в виде списка
Car1 = namedtuple('Car1', ['make', 'model', 'year'])

# Пример с указанием полей в виде кортежа
Car2 = namedtuple('Car2', ('make', 'model', 'year'))

# Пример с указанием полей в виде строки, разделенной пробелами
Car3 = namedtuple('Car3', 'make model year')

# Пример с указанием полей в виде строки, разделенной запятыми
Car4 = namedtuple('Car4', 'make, model, year')