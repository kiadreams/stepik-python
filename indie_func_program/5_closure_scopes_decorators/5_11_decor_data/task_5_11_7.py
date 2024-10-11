from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def inner(*args, **kwargs):
        args = ['Monkey' for _ in args]
        kwargs = {k: 'patching' for k in kwargs}
        return func(*args, **kwargs)

    return inner


@monkey_patching
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(concatenate('my', 'name is', 'Artem'))
print(concatenate.__name__)
print(concatenate.__doc__.strip())