class TypeValidation:

    def __init__(self, data_type):
        self.data_type = data_type

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise ValueError(f'В атрибут {self.attribute_name} можно '
                             f'сохранять только тип {self.data_type.__name__}')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)


# Проверка работы дескриптора-------------------------------------------------
class Person:
    age = TypeValidation(int)
    height = TypeValidation(float)
    name = TypeValidation(str)
    hobbies = TypeValidation(list)
