class StringValidation:
    def __init__(self,
                 min_length=None,
                 max_length=None,
                 exclude_chars=None,
                 is_same_register=False):
        self.min_length = min_length
        self.max_length = max_length
        self.exclude_chars = exclude_chars
        self.is_same_register = is_same_register

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
        if isinstance(self.min_length, int) and len(value) < self.min_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не меньше {self.min_length} символов')
        if isinstance(self.max_length, int) and len(value) > self.max_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не больше {self.max_length} символов')
        if (isinstance(self.exclude_chars, str)
            and any([i in value for i in self.exclude_chars])):
            raise ValueError(f'Имеются недопустимые символы в атрибуте '
                             f'{self.attribute_name}')
        if self.is_same_register and not (value.islower() or value.isupper()):
            raise ValueError(f'Все буквы должны быть в одном регистре в '
                             f'атрибуте {self.attribute_name}')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)


# Проверка работы дескриптора------------------------------------------------
class Person:
    name = StringValidation(is_same_register=True, exclude_chars='tyur')
    last_name = StringValidation(max_length=10, is_same_register=True)


p = Person()
try:
    p.name = 'Michail Second'
except ValueError as ex:
    print(ex)
try:
    p.last_name = 'LERMONTOV'
except ValueError as ex:
    print(ex)
print(p.name, p.last_name)