"""
    Определяется это значением метакласса, оно имеется у каждого класса. Мы его
не видели до этого момента, потому что оно определяется не явно и принимает
значение type.
    Явное определение класса Person со значением метакласса выглядит следующим
образом:
"""
class Person(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} year old.'


"""В нем видно, что родителем является object, а метаклассом — type.
Аргумент metaclass позволяет нам указать, какой класс мы хотим использовать для
создания нашего класса. Таким образом, мы могли бы создать собственный класс, 
который будет создавать новый тип данных, внедряя в процесс создания любую 
функциональность, которую мы хотим. Это позволит нам изменять 
определение/функциональность класса, который мы создаем, с помощью кода.

Python вызовет наш метакласс с теми же аргументами, которые он передаст 
конструктору type: name, bases и class_dict, поэтому нам нужно обязательно 
описать эти аргументы в определении метакласса.  Остальную работу по созданию 
словаря классов и выполнению кода в этом контексте, проставление имени класса 
и родителей метакласс берет на себя.
"""


class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        print('Запуск создания нового типа данных!')
        # делегируем создание объекта через super (в данном случае родитель это класс type)
        cls_obj = super().__new__(cls, name, bases, class_dict)
        cls_obj.say_hello = lambda self: f"Hello, my name is {self.name}"
        return cls_obj


class Person(metaclass=CustomType):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} year old.'


print(Person)
print('Type of Person is', type(Person))
print('Person is isinstance of CustomType', isinstance(Person, CustomType))
print('Person is isinstance of type', isinstance(Person, type))

p = Person('Ivan', 25)
print(p.greeting())
print(p.say_hello())