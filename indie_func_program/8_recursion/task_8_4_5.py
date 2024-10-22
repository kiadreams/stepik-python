def is_member(value, lst):
    for i in lst:
        if isinstance(i, list):
            if is_member(value, i):
                return True
        else:
            if i == value:
                return True
    return False


print(is_member(5, [1, 2, 3, 4, 5]))
print(is_member(8, [[1, 2, 3], [4, [5, 6]], 7]))
print()



def is_member1(num: int, lst: list)->bool:
    for value in lst:
        if isinstance(value, int) and value == num: return True
        if isinstance(value, list): return is_member(num, value)
    return False


print(is_member1(5, [1, 2, 3, 4, 5]))
print(is_member1(8, [[1, 2, 3], [4, [5, 6]], 7]))
