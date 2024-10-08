def return_5():
    return 5

def my_decor(f):
    return return_5


@my_decor
def some_func():
    print("s")


print(some_func())
