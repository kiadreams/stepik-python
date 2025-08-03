m = [list(input()) for _ in range(8)]
i, j = [(i, j) for i, e in enumerate(m) for j, s in enumerate(e) if s == 'F'].pop()
for y in range(8):
    for x in range(8):
        if i == y and j == x:
            pass
        elif (i - y == j - x) or (y + x == i + j):
            m[y][x] = '+'
        elif x == j or y == i:
            m[y][x] = "+"
        print(m[y][x], end='')
    print()
