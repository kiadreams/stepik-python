# from math import factorial
#
# summa = 0
# for i in range(50, 101):
#     summa += i**3
# print(summa)
#
# print("adfasdf".index('f'))
# filter()
# min()


# Интересная конструкция!!!!
# n, nums = int(input()), list(map(int, input().split()))
# [print(min(nums), end=' ') or nums.remove(min(nums)) for _ in range(n)]

a = [7, 8, 1]
print(min(a)) or a.remove(min(a))
print(a)