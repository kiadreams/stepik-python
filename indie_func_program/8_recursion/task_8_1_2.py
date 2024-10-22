def print_from(n):
    print(n)
    if n > 1:
        print_from(n - 1)


print_from(5)
