def sum_recursive(l: list[int | list[int]]) -> int:
    total = 0
    for i in l:
        if isinstance(i, list):
            total += sum_recursive(i)
        else:
            total += i
    return total


print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))