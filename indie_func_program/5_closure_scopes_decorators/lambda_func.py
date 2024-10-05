print((lambda: 'hello')())
print()


surprise = lambda: print('surprise')
print(surprise())
print()


some_prints = lambda: (
    print('Hello world'),
    print(1, 2, 3),
    print(4, 5)
)

some_prints()