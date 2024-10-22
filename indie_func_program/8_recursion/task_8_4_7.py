def reversed_recursive(l):
    return [reversed_recursive(i) if isinstance(i, list) else i
            for i in reversed(l)]


print(reversed_recursive([1, 2, 3, 4, 5]))
print(reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
print(reversed_recursive([[1, 2, 3], [4, [5, [6]]], 7]))