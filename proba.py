# import calendar as cl
# from datetime import datetime
# from typing import Callable, Any
#
#
# def get_the_fastest_func(funcs: list[Callable[Any, Any]], arg: Any) -> Callable:

import time


def time_of(func, count=100):
    start = time.perf_counter()
    func(count)
    end = time.perf_counter()
    print(end - start)


def my_func_append(count: int):
    lst = []
    for i in range(count):
        lst.append(1)

def my_func_insert(count: int):
    lst = []
    for i in range(count):
        lst.insert(0, i)

# time_of(my_func_insert, 1_000_000)
team = ['Arthur', 'Timur', 'Anton', 'Valera', 'Arthur', 'Sveta']
lengths = [len(name) for name in team]

print(*lengths)