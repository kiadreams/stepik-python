result = {}
for num in range(1, int(input()) + 1):
    sum_numbers = sum([int(i) for i in str(num)])
    result[sum_numbers] = result.get(sum_numbers, 0) + 1
print(sorted(result.values())[-1])
