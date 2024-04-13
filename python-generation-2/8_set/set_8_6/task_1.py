numbers_1, numbers_2 = (input().split() for _ in range(2))
result = set(numbers_1).intersection(numbers_2)
print(len(result))