from functools import wraps


def validate_all_args(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all(isinstance(el, type_) for el in args):
                return func(*args, **kwargs)
            print(f"Все аргументы должны принадлежать типу {type_}")
            return None

        return wrapper

    return decorator


@validate_all_args(str)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)


@validate_all_args(int)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
