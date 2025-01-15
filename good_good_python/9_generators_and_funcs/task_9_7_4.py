lst_in = [
    'Номер;Имя;Оценка;Зачет',
    '1;Портос;5;Да',
    '2;Арамис;3;Да',
    '3;Атос;4;Да',
    "4;д'Артаньян;2;Нет",
    '5;Балакирев;1;Нет',
]


def tp_sort(x):
    dict_value = {'Имя': 1, 'Зачет': 2, 'Оценка': 3, 'Номер': 4}
    return dict_value[x[0]]


lst_1 = lst_in[0].split(';')
lst_2 = [
    [int(e[0]), e[1], int(e[2]), e[3]]
    for e in [i.split(';') for i in lst_in[1:]]
]
zip_lst = list(zip(lst_1, *lst_2))
print(zip_lst)
t_sort = tuple(zip(*sorted(zip_lst, key=tp_sort)))




