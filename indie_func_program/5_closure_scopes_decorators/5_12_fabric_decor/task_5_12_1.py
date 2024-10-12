from functools import wraps


def multiply_result_by(n):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * n

        return inner

    return decorator


@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))
