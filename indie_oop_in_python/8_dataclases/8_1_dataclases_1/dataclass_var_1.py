from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int


artem = Person("Artem", "Egorov", 33)
print(artem.first_name)
print(artem.last_name)
print(artem.age)
print(artem)
