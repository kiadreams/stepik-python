class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = None


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)  # делегирование
        self.age = age  # логика


d = Doctor('Sheldon', 'Cooper', 14)
print(d.name, d.surname, d.age)