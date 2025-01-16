import random, pprint
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 7
P = [[0] * N for i in range(N)]


# здесь продолжайте программу
M = 10
n = 0


def get_cords(x):
    x_min = x - 1 if x > 0 else 0
    x_max = x + 1 if x < 9 else 9
    return x_min, x_max + 1


def is_free(i: int, j: int) -> bool:
    i_min, i_max = get_cords(i)
    j_min, j_max = get_cords(j)
    lines = P[i_min:i_max]
    sum_elms_of_lines = [sum(e[j_min:j_max]) for e in lines]
    return sum(sum_elms_of_lines) == 0


while n < M:
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    if is_free(i, j):
        P[i][j] = 1
        n += 1


pprint.pprint(P)
