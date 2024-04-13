def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)

my_func(a=13, b=15)
print()
my_func(17, 15, 34, d=24, c=12)