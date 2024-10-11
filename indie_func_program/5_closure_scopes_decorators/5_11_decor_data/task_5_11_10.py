from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        values = (*args, *kwargs.items())
        if values in cache:
            print(f'[FROM CACHE] Вызов {func.__name__} = {cache[values]}')
        return cache.setdefault(values, func(*args, **kwargs))

    return inner


@cache_result
def multiply(a, b):
    return a * b


print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(5, 4))
print(multiply.__name__)
