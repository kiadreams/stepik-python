def get_square_and_cube(num: int) -> tuple[int, int]:
    return num ** 2, num ** 3


a = [-1, 2, -3, 4, -5]
b = list(map(get_square_and_cube, a))
c = [(i**2, i**3) for i in a]
print(b)
print(c)

print('.'.join('sdfsd'))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))
print(result)

result2 = list(map(sum, zip(nums1, nums2, nums3)))
print(result2)

