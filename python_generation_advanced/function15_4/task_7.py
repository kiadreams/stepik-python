numbers = [i for i in input().split()]

def my_key(x):
    value = sum(map(int, x))
    return value, int(x)

print(*sorted(numbers, key=my_key))
