def print_given(*args, **kargs):
    for arg in args:
        print(arg, type(arg))
    for key, value in sorted(kargs.items()):
        print(key, value, type(value))


print_given(1, [1, 2, 3], 'three', two=2)
# print_given('apple', 'cherry', 'watermelon')
