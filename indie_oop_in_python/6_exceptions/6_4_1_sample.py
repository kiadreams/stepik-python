try:
    [1, 2, 4][5]
except (KeyError, IndexError) as error:
    print(f"Logging error: {repr(error)}")
    raise TypeError("ошибка типа") from None
except ZeroDivisionError as err:
    print("ZeroDivisionError")
    print(f"Logging error: {err} {repr(err)}")