list_numbers = [set(map(int, input())) for _ in range(int(input()))]
result = list_numbers[0].intersection(*list_numbers)
print(*sorted(result))
