numbers = [8, 11, -5, 4, 3]

def get_rec_sum(nums: list):
    return nums[-1] + get_rec_sum(nums[:-1]) if nums else 0

print(get_rec_sum(numbers))