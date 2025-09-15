from collections import Counter


def compare_lists(lst1: list, lst2: list) -> bool:
    return Counter(lst1) == Counter(lst2)


assert compare_lists([1, 2, 3, 4], [4, 3, 2, 1])
assert not compare_lists([1, 2, 3], [4, 5, 6])
assert not compare_lists([1, 2, 3], [1, 2, 3, 4])
assert compare_lists([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [4, 4, 3, 3, 2, 2, 1, 4, 3, 4])
assert compare_lists([1, 1, 2, 2, 1], [2, 2, 1, 1, 1])
assert not compare_lists([1, 1, 2, 2], [2, 1, 1, 1])
