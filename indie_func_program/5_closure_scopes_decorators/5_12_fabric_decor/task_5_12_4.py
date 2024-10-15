from functools import wraps


def pass_arguments(*dargs, **dkwargs):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            args = [*args, *dargs]
            kwargs = {**kwargs, **dkwargs}
            return func(*args, **kwargs)

        return inner

    return decorator


@pass_arguments(s='Когда', w='-', r='нибудь!')
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
