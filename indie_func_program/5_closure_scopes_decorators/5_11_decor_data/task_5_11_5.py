from functools import wraps


def explicit_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args:
            print('Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений')
            return None
        return func(*args, **kwargs)

    return inner


@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add(a=10, b=20))
