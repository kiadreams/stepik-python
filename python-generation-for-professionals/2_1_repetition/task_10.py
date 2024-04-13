def choose_plural(amount: int, declensions: tuple) -> str:
    div_100, div_10, result = amount % 100, amount % 10, 0
    if div_100 in range(11, 20) or div_10 in [5, 6, 7, 8, 9, 0]:
        result = 2
    elif div_10 in [2, 3, 4]:
        result = 1
    return f'{amount} {declensions[result]}'


print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
