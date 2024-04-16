# Первый вариант...
nums = [int(x) for x in input().split()]
for num in set(nums):
    nums.remove(num)
# if nums:
print(*sorted(set(nums)))


# Второй вариант...
# nums = [int(x) for x in input().split()]
# uniq_nums = sorted(filter(lambda x: nums.count(x) > 1, set(nums)))
# print(*uniq_nums)