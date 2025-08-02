class StringValidation:

    def __init__(self, min_len):
        self.min_len = min_len

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        if len(value) < self.min_len:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не меньше {self.min_len} символов')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)