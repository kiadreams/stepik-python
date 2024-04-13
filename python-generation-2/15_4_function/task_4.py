athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def choose_sort(num):
    return lambda x: x[num - 1]


type_sort = int(input())
athletes.sort(key=choose_sort(type_sort))
for athlete in athletes:
    print(*athlete)