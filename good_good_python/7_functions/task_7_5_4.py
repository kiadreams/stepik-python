lst2D = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]


def verify(lst2d) -> bool:
    for i in range(len(lst2d) - 1):
        for j in range(len(lst2d) - 1):
            m = [sum(row[j: j + 2]) for row in lst2d[i:i + 2]]
            if not is_isolate(m):
                return False
    return True


def is_isolate(m) -> bool:
    return sum(m) < 2


# здесь продолжайте программу по формированию двумерного списка lst2D

print(lst2D)
print(verify(lst2D))
# lst2D = [list(map(int, l.split())) for l in lines]