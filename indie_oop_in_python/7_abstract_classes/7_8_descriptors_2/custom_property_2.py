class CustomProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable.')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable.')
        self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self


class Person:
    @CustomProperty
    def first_name(self):
        return getattr(self, '_first_name', None)

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @CustomProperty
    def last_name(self):
        return getattr(self, '_last_name', None)

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


p = Person()
print(p.__dict__)
p.first_name = 'Artem'
p.last_name = 'Egorov'
print(p.__dict__)

# пробуем затемнить дескриптор
p.__dict__['first_name'] = 'Egor'
print(p.first_name, p.last_name)
