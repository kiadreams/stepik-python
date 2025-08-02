class StringValidation:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        if len(value) < self.min_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не меньше {self.min_length} символов')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)


class Person:
    name = StringValidation(5)
    last_name = StringValidation(7)


p = Person()
p.name = 'Michail'
p.last_name = 'Lermontov'
print(p.name, p.last_name)
try:
    p.name = 'M.'
except ValueError as ex:
    print(ex)
print(p.name, p.last_name)