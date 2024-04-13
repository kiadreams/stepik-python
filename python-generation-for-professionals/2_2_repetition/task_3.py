# # Мой вариант...
# def revers_list(lst, start, end):
#     start, end = start - 1, end - 1
#     for i in range((end - start + 1) // 2):
#         lst[start + i], lst[end - i] = lst[end - i], lst[start + i]


# n, x, y, a, b = [int(i) for i in input().split()]
# nums = list(range(1, n + 1))
# revers_list(nums, x, y)
# revers_list(nums, a, b)
# print(*nums)

# Вариант преподавателя...
n, x, y, a, b = [int(i) for i in input().split()]
nums = list(range(1, n + 1))
nums[x - 1: y] = reversed(nums[x - 1: y])
nums[a - 1: b] = reversed(nums[a - 1: b])
print(*nums)
