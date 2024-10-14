from functools import wraps


def counting_calls(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.call_count += 1
        inner.calls.append({'args': args, 'kwargs': kwargs})
        return func(*args, **kwargs)

    inner.call_count = 0
    inner.calls = []
    return inner


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])