numbers_1, numbers_2 = (list(map(int, input().split())) for _ in range(2))
result = set(numbers_1).intersection(numbers_2)
print(*sorted(result))