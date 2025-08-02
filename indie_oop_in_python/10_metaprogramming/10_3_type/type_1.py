class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} year old.'


print(isinstance(Person, type))
print(isinstance(Person, object))
print()
print(isinstance(object, type), object, type)
print(isinstance(type, object), type(object), type(type))
print(type(Person))