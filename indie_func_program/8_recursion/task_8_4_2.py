def multu_recursive(l):
    total = 1
    for i in l:
        if isinstance(i, list):
            total *= multu_recursive(i)
        elif isinstance(i, int):
            total *= i
    return total


print(multu_recursive(['1', '2', '3', '4', '5']))
print(multu_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))