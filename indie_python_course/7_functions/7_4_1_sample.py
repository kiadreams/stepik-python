value = 10


def foo():
    global value
    value = 5
    value += 1


print(value)
foo()
print(value)
print('\n')

# ___________________________________________________________________________

v = 10


def foo1():
    v = 5
    global v
    v += 1


print(value)