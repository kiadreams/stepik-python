class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def greeting(self):
    return f'Hi, I am {self.name}. I am {self.age} year old.'
"""

class_namespace = {}

exec(class_body, globals(), class_namespace)

class_name = 'Person'
class_bases = tuple()  # пустой кортеж, значит наследуемся от object
Person = type(class_name, class_bases, class_namespace)

print(Person)
print(type(Person))
print(Person.__dict__)