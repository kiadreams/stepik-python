from functools import wraps


def add_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func('begin', *args, 'end', **kwargs)

    return inner
