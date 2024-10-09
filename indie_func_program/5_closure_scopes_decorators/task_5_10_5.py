def validate_all_args_str(func):

    def wrapper(*args, **kwargs):
        if all(isinstance(el, str) for el in args):
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
            return None

    return wrapper


@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))