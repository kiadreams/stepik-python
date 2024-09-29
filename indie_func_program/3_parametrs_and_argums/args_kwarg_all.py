def my_func(a, b, *, c, d):
    print(f"{a=}, {b=}, {c=}, {d=}")


my_func(1, 2, c=3, d=4)
my_func(1, 2, d=4, c=3)
my_func(1, c=3, d=4, b=2)
my_func(a=1, c=3, d=4, b=2)

print()


def my_func(a, b=2, *args, c=3, d):
    print(f"{a=}, {b=}, {args=}, {c=}, {d=}")


my_func(1, 3, "q", "w", "e", "r", c=3, d=4)
my_func(1, "q", "w", "e", "r", c=3, d=4)

print()


def my_func(a, b, *, c, d=4, **kwargs):
    print(f"{a=}, {b=}, {c=}, {d=}, {kwargs=}")


my_func(1, 2, c=3, q=10, w=20, e=30)
my_func(q=10, w=20, e=30, c=3, b=2, a=1)

print()


def my_func(*args, **kwargs):
    print(f"{args=}, {kwargs=}")


my_func(1, 2, "q", "w", "e", "r", c=3, d=5, q=10, w=20, e=30)
