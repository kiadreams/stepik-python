from collections import Counter


def find_three_most_common(lst: list) -> list:
    common_lst = [value for value, _ in Counter(lst).most_common(3)]
    common_lst += [None] * (3 - len(common_lst))
    return list(reversed(common_lst))


assert find_three_most_common([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]
assert find_three_most_common([1, 1, 1, 1, 1]) == [None, None, 1]
assert find_three_most_common([1, 1, 1, 2, 2]) == [None, 2, 1]
assert find_three_most_common([1, 1, 2, 2, 2]) == [None, 1, 2]
assert find_three_most_common([]) == [None, None, None]
