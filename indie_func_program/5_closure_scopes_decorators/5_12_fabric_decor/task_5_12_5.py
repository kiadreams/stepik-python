from functools import wraps


def convert_to(type_):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return type_(func(*args, **kwargs))

        return inner

    return decorator


@convert_to(int)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")
