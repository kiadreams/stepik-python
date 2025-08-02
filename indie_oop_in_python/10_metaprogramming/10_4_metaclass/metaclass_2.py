class Metaclass(type):
    def __new__(cls, name, bases, cls_dict, arg1, arg2, arg3=None):
        print('Запуск создания нового типа данных', arg1, arg2, arg3)
        return super().__new__(cls, name, bases, cls_dict)


class MyClass1(metaclass=Metaclass, arg1=10, arg2=20, arg3=30):
    pass


class MyClass2(metaclass=Metaclass, arg1=1, arg2=5):
    pass


"""
Но что, если мы хотим передать дополнительные аргументы методу __new__ нашего 
метакласса. Можем ли мы так сделать?

Начиная с версии python 3.6, ответ на данный вопрос положительный. Но есть 
ограничение на такие параметры, которое состоит в том, что они должны 
передаваться как именованные аргументы (позиционные аргументы используются 
для указания родительских классов).
"""