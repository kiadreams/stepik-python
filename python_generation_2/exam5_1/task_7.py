string = input()
x, y = 8 - int(string[1]), ord(string[0]) - 97
field = [['.'] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i == x or j == y:
            field[i][j] = '*'
        elif abs(i - x) == abs(j - y):
            field[i][j] = '*'
field[x][y] = 'Q'
for elem in field:
    print(*elem)
