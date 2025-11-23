from math import factorial
from collections import UserDict
from typing import Callable


# Напишите определение класса ExtraDict
class ExtraDict(UserDict):

    def map(self, func: Callable[[int], int]) -> None:
        for key, value in self.items():
            self[key] = func(value)

    def remove(self, key: str) -> None:
        del self[key]

    def is_empty(self) -> bool:
        return not len(self)


my_dict = ExtraDict({'a': 1, 'b': 2, 'c': 3})
print("Original dictionary:", my_dict.data)

my_dict.map(lambda x: x * 2)
print("Dictionary after applying 'map':", my_dict.data)

my_dict.map(factorial)
print("Dictionary after applying factorial:", my_dict.data)

my_dict.remove('b')
my_dict.pop('c')

assert not my_dict.is_empty()

my_dict.remove('a')

assert my_dict.is_empty()

try:
    my_dict.remove('a')
except KeyError:
    pass
