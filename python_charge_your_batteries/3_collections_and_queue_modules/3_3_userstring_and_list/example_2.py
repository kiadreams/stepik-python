from collections import UserList
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


class StringList(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def insert(self, index, item):
        self.data.insert(index, str(item))

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)


strings = StringList([1, 2, 'hello', Person('Jack', 32), True])
print(strings)
strings.append(20)
strings.insert(0, 100)
strings.extend([3, 4, 5])
print(strings)
