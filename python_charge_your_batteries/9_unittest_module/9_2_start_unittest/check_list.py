def is_sorted_ascending(lst: list) -> bool:
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


def is_sorted_descending(lst: list) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))