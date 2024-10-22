# Первый вариант
def find_level_element1(value, l):
    level = 1
    for v in l:
        if isinstance(v, list):
            n_lev = find_level_element(value, v)
            if n_lev > 0:
                return level + n_lev
        else:
            if v == value:
                return level
    return level - 2


# Второй вариант
def find_level_element(value, l):
    for i in l:
        if isinstance(i, list):
            if (level := find_level_element(value, i)) > 0:
                return level + 1
        else:
            if i == value:
                return 1
    return -1


print(find_level_element(5, [1, 2, 3, 4, [[[5]]], [5]]))
print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))