from functools import wraps


def add_attrs(**d_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for k, v in d_kwargs.items():
            setattr(wrapper, k, v)
        return wrapper

    return decorator


@add_attrs(test=True, ordered=True)
def add(a, b):
    return a + b


print(add(10, 5))
print(add.test)
print(add.ordered)
