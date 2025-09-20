from collections import Counter


def find_difference_with_counter(lst1: list, lst2: list) -> list:
    return sorted((Counter(lst1) - Counter(lst2)).elements())
    # counter = Counter(lst1)
    # counter.subtract(lst2)
    # return sorted(counter.elements())


assert find_difference_with_counter([1, 2, 2, 3, 4, 4, 5],
                                    [2, 3, 3, 4, 5, 6]) == [1, 2, 4]

assert find_difference_with_counter([5, 4, 5, 1, 2, 7, 3],
                                    [2, 3, 3, 4, 5, 6]) == [1, 5, 7]

assert find_difference_with_counter([1, 1, 2, 3, 3, 4, 4, 5, 6, 7],
                                    [1, 1, 2, 4, 5, 6]) == [3, 3, 4, 7]

assert find_difference_with_counter([1, 1, 1, 1],
                                    [1, 1, ]) == [1, 1]

assert find_difference_with_counter([1, 1, ],
                                    [1, 1, 1, 1]) == []