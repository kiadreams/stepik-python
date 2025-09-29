
"""
Метод __missing__ вызывается при обращении к несуществующему
ключу, мы можем переопределить значения по умолчанию при обращении к
несуществующему ключу.
"""


class MyDict(dict):
    def __missing__(self, key):
        return f"The key '{key}' does not exist in the dictionary"


my_dict = MyDict({'a': 1, 'b': 2})
print(my_dict['d'])