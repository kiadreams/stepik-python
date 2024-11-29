# import sys

# считывание списка из входного потока
lst_in = [list(map(int, input().strip().split())) for _ in range(5)]


# здесь продолжайте программу (используйте список lst_in)
is_exist = False
for i in range(4):
    if is_exist:
        break
    for j in range(4):
        if sum([*lst_in[i][j: j + 2], *lst_in[i + 1][j: j + 2]]) > 1:
            is_exist = True
            break
print(('ДА', 'НЕТ')[is_exist])
