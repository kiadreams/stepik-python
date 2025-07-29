class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def description(self):
    return f'{self.name} is {self.age} years old'

def speak(self, sound):
    return f'{self.name} says {sound}'
"""
class_namespace = {}

exec(class_body, globals(), class_namespace)

Dog = type('Dog', tuple(), class_namespace)


# Проверка работы кода--------------------------------------------------------
print(Dog, type(Dog))