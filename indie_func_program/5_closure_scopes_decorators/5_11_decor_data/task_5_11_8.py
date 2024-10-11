from functools import wraps


def counting_calls(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.call_count += 1
        return func(*args, **kwargs)

    inner.call_count = 0
    return inner


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print(add.call_count)
print(add(30, 5))
print(add.call_count)
