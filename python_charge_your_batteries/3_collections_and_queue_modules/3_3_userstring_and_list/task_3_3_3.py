from collections import UserList
from typing import Callable


# Напишите определение класса MyList
class MyList(UserList):

    def shift_left(self) -> None:
        self.data = self.data[1:] = self.data[:1]

    def shift_right(self) -> None:
        self.data = self.data[:-1] + self.data[-1:]

    def for_each(self, func: Callable[[int], int]) -> None:
        self.data = list(map(func, self.data))


# Проверки для класса MyList

my_list = MyList([1, 2, 3, 4, 5])

assert my_list.data == [1, 2, 3, 4, 5]

my_list.shift_left()
assert my_list.data == [2, 3, 4, 5, 1]
my_list.shift_left()
my_list.shift_left()
assert my_list.data == [4, 5, 1, 2, 3]

my_list.shift_right()
assert my_list.data == [3, 4, 5, 1, 2]

my_list.for_each(lambda x: x ** 2)
assert my_list.data == [9, 16, 25, 1, 4]
