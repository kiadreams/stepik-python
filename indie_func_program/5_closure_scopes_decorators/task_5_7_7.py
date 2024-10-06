def filter_collection(func, colect):
    if isinstance(colect, list):
        return [i for i in colect if func(i)]
    elif isinstance(colect, tuple):
        return tuple(i for i in colect if func(i))
    elif isinstance(colect, dict):
        return {itm[0]: itm[1] for itm in colect.items if func(itm)}
    elif isinstance(colect, str):
        return ''.join([i for i in colect if func(i)])


def is_even(num):
    return num % 2 == 0


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = filter_collection(is_even, numbers)
print(even_numbers)