from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


count = 0
while (some_date := input()) != 'end':
    if is_correct(*[int(n) for n in some_date.split('.')]):
        count += 1
        print('Корректная')
    else:
        print('Некорректная')
print(count)