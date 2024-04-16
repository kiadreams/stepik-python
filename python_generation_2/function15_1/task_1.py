def matrix(rows=1, columns=None, value=0):
    if not columns:
        columns = rows
    return [[value for _ in range(columns)] for _ in range(rows)]


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(columns=5))
print(matrix(3, 4, 9))