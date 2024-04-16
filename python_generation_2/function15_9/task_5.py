from operator import mod

# Вариант №1:
# a, b = int(input()), int(input())
# result = []
# for num in range(a, b + 1):
#     str_num = str(num)
#     if '0' in str_num:
#         continue
#     if all(map(lambda x: num % int(x) == 0, str_num)):
#         result.append(num)
# print(*result)


# Вариант №2:
a, b = int(input()), int(input())
check_func = lambda num: all(int(s) and num % int(s) == 0 for s in str(num))
result = filter(check_func, range(a, b + 1))
print(*result)
