class Person_slots:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


p_slots = Person_slots('ivan', 'sdf', 34)
p = Person('Igor', 'sdfg', 38)

print(p_slots.__sizeof__(), p.__sizeof__())
print(p_slots.__slots__.__sizeof__(), p.__dict__.__sizeof__())
print(dir(p_slots))
print()
print(dir(p))