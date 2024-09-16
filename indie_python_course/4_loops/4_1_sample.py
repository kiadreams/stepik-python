# a, b = int(input()), int(input())
# while a < b:
#     if a % 2 == 0 or a % 3 == 0:
#         a += 1
#         continue
#     if a % 777 == 0:
#         break
#     print(a)
#     a += 1


nums = [int(x) for x in input().split()]
print(nums == sorted(nums))

