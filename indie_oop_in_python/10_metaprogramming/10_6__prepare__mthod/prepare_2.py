class MyMeta(type):
    def __prepare__(name, bases, **kwargs):
        print(f'MyMeta.__prepare__ called... with {kwargs}')
        print()
        kwargs['bonus_attr'] = 'Hello'
        return kwargs

    def __new__(cls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('cls: ', cls, type(cls))
        print('name:', name, type(name))
        print('bases: ', bases, type(bases))
        print('cls_dict:', cls_dict, type(cls_dict))
        print('kwargs:', kwargs)
        print()
        return super().__new__(cls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta, arg1=10, arg2=15):
    pass


print(MyClass.__dict__)


"""
    Как видите, все, что мы передавали в параметрах метакласса, и также 
дополнительный атрибут bonus_attr, имеется в атрибутах класса, и нам не нужно 
было использовать метод __new__ для их создания. Очень часто `__prepare__` 
является гораздо более простой альтернативой переопределению атрибутов чем 
метод `__new__`.
    Возвращаемое значение `__prepare__` должно быть типом mapping.
"""