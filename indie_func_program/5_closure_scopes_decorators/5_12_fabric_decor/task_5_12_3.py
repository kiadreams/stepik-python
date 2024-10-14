from functools import wraps


def monkey_patching(arg="Monkey", kwarg="patching"):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            args = [arg for _ in args]
            kwargs = {k: kwarg for k in kwargs}
            return func(*args, **kwargs)

        return inner

    return decorator
