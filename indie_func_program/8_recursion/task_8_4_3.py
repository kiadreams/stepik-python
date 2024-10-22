# Первое решение...
def get_max_recursive1(l):
    max_value = l[0] if isinstance(l[0], int) else get_max_recursive(l[0])
    for i in l[1:]:
        if isinstance(i, list):
            next_value = get_max_recursive(i)
            max_value = next_value if next_value > max_value else max_value
        else:
            max_value = i if i > max_value else max_value
    return max_value


def get_max_recursive(l):
    max_value = float('-inf')
    for i in l:
        if isinstance(i, list):
            if (next_value := get_max_recursive(i)) > max_value:
                max_value = next_value
        else:
            if i > max_value:
                max_value = i
    return max_value


print(get_max_recursive1([1, 2, 3, 4, 5]))
print(get_max_recursive1([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(get_max_recursive1([-1, -2, -3, -4, -5]))
print()
print(get_max_recursive([1, 2, 3, 4, 5]))
print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(get_max_recursive([-1, -2, -3, -4, -5]))
print()


# Чужое решение
def get_max_recursive3(lst):
    maximum = 0
    for value in lst:
        match value:
            case list():
                ans = get_max_recursive(value)
                if ans > maximum: maximum = ans
            case int():
                if value > maximum: maximum = value
    return maximum


print(get_max_recursive3([-1, -2, -3, -4, -5]))
