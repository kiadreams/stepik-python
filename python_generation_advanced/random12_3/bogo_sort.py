import random


def is_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogo_sort(nums):
    while not is_sort(nums):
        random.shuffle(nums)
    return nums


numbers = list(range(10))
random.shuffle(numbers)
print(numbers)

sorted_numbers = bogo_sort(numbers)
print(sorted_numbers)
