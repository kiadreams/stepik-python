try:
    raise ValueError("ошибка значения")
except ValueError as first:
    try:
        raise TypeError("ошибка типа")
    except TypeError as second:
        raise Exception("Большое исключение") from first
