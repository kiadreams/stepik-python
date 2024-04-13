numbers = [i for i in input().split()]
my_key = lambda x: sum(map(int, x))
print(*sorted(numbers, key=my_key))