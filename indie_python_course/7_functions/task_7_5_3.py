def create_matrix(size=3, up_fill=0, down_fill=0):
    m = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                m[i][j] = i + 1
            else:
                m[i][j] = up_fill if j > i else down_fill
    return m


print(create_matrix(up_fill=7, down_fill=3))