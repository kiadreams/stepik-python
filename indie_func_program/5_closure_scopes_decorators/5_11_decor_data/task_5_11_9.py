from functools import wraps


def check_count_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        sum_args = len(args) + len(kwargs)
        if sum_args == 2:
            return func(*args, **kwargs)
        if sum_args > 2:
            print('Too many arguments')
        else:
            print('Not enough arguments')
        return None

    return inner


@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


print(add_numbers(4, 5))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())
