class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        print('Запуск создания нового типа данных!')
        # делегируем создание объекта через super (в данном случае родитель это класс type)
        cls_obj = super().__new__(cls, name, bases, class_dict)
        cls_obj.say_hello = lambda self: f"Hello, my name is {self.name}"
        return cls_obj


class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def greeting(self):
    return f'Hi, I am {self.name}. I am {self.age} year old.'
"""

class_namespace = {}
exec(class_body, globals(), class_namespace)

Person = CustomType('Person', (), class_namespace)

print(Person)
print('Type of Person is', type(Person))
print('Person is isinstance of CustomType', isinstance(Person, CustomType))
print('Person is isinstance of type', isinstance(Person, type))

p = Person('Ivan', 25)
print(p.greeting())
print(p.say_hello())