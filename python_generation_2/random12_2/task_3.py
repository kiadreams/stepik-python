from random import shuffle


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
n, k = len(matrix[0]), len(matrix)
indices = list(range(n * k))
shuffle(indices)
for i in range(k):
    for j in range(n):
        i_1, j_1 = divmod(indices[i * k + j], k)
        matrix[i][j], matrix[i_1][j_1] = matrix[i_1][j_1], matrix[i][j]
