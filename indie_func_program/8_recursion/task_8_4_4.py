def flatten(l):
    res = []
    for i in l:
        if isinstance(i, list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res


print(flatten([1, [2, 3], [[2], 5], 6]))
