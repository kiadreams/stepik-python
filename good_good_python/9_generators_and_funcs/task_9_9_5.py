lst_in = ['# x o', 'x # x', 'o o #']

pole = [i.split() for i in lst_in]


def is_free(lst):
    return any('#' in e for e in lst)

print(is_free(pole))