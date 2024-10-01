x = 1


def my_func():
    a = 1
    b = 2
    c = 3
    print(globals())


my_func()
print(globals())

y = 2

my_func()
print(globals())