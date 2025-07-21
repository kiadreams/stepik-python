from dataclasses import make_dataclass

Person = make_dataclass('Person', ['first_name', 'last_name', 'age'])


artem = Person('Artem', 'Egorov', 33)
print(artem.first_name)
print(artem.last_name)
print(artem.age)
print(artem)

# или
Person = make_dataclass(
    'Person',
    [
        ('first_name', str),
        ('last_name', str),
        ('age', int)
    ]
)

artem = Person('Artem', 'Egorov', 33)
print(artem.first_name)
print(artem.last_name)
print(artem.age)
print(artem)