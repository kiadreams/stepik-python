from typing import NamedTuple
from datetime import date


class Person(NamedTuple):
    name: str
    birth_date: date
    country: str


person = Person('Megan Jones', '1987-07-16', 'Bolivia')

print(person.name)  # Выводит: 'Megan Jones'
print(person.birth_date)  # Выводит: 1987-07-16
print(person.country)  # Выводит: Bolivia
