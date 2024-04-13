def mean(*args):
    numbers = [num for num in args if type(num) in (int, float)]
    return 0 if not numbers else sum(numbers) / len(numbers)


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print()
n = 0
print(n or 1)