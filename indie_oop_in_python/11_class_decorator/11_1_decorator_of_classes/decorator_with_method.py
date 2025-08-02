def add_hello(cls):
    cls.hello = lambda self: f'{self} says hello!'
    return cls


@add_hello
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


p = Person('Guido')
print(p.hello())