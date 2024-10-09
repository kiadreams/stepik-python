def is_arg_correct(value):
    if isinstance(value, int):
        return value == 0 or not value % 2
    return value and len(value) % 2 == 0


def filter_even(func):
    def wrapper(*args, **kwargs):
        args = [el for el in args if is_arg_correct(el)]
        return func(*args, **kwargs)

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if isinstance(k, str) and
                  len(k) > 4}
        return func(*args, **kwargs)

    return wrapper


@filter_even
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))

# Correct output:
# НуПитон?
