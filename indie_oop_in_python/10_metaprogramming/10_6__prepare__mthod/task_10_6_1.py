class CustomDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


class MyMeta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        d = CustomDict()
        d['weapon'] = 'blaster'
        d['health'] = 100
        return d

    def __new__(cls, name, bases, cls_dict):
        return super().__new__(cls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta):
    pass


assert hasattr(MyClass, 'weapon')
assert hasattr(MyClass, 'health')

print('Good')