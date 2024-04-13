info_1 = {1: [1, 2, 3,], 2: [4, 5, 6], 3: [7, 8, 9]}
info_2 = info_1.copy()

print(info_1, info_2)
info_2[1][0] = 33
print(info_1, info_2)
info_1[1] = [1, 2, 3]
print(info_1, info_2)
