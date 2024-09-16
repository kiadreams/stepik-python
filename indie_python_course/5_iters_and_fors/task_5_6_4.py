# Пузырьковая сортировака!!!

count = 0
n = int(input())
numbers = list(map(int, input().split()))
for i in range(n, 0, -1):
    for j in range(i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            count += 1
print(*numbers)
print(count)
