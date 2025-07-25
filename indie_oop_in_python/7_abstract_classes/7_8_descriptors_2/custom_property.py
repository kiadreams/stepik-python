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


class Person:
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    name = CustomProperty(fget=get_name, fset=set_name)


p = Person()
print(p.__dict__)
p.name = 'Artem'
print(p.name)
print(p.__dict__)

# пробуем затемнить дескриптор
p.__dict__['name'] = 'Egor'
print(p.name)
print()
print(p.__dict__)