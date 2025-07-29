class MyMeta(type):

    @staticmethod
    def __prepare__(name, bases, **kwargs):
        print('MyMeta.__prepare__ called...')
        print('name:', name)
        print('bases:', bases)
        print('kwargs:', kwargs)
        print()
        return {'NAME': 'Billy', 'age': 33}

    def __new__(cls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('cls: ', cls, type(cls))
        print('name:', name, type(name))
        print('bases: ', bases, type(bases))
        print('cls_dict:', cls_dict, type(cls_dict))
        print('kwargs:', kwargs)
        return super().__new__(cls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta, kw1=10, kw2=20):
    pass
