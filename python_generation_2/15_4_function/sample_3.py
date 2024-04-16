def square_add_one(x):
    return x*x + 1


def cube_add_square(x):
    return x**3 + x**2


def plot(f, a=10, b=10):
    print(type(f))
    print(f(a), '\n')
    
plot(cube_add_square)


numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers))
print(min(numbers))
print(sorted(numbers), '\n')


print(max(numbers, key=abs))  # указываем функцию abs в качестве компаратора
print(min(numbers, key=abs))  # указываем функцию abs в качестве компаратора
print(sorted(numbers, key=abs), '\n')  # указываем функцию abs в качестве компаратора

print(-4 ** 2 +1)