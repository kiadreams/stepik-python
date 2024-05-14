m, n = int(input()), int(input())
my_books = [input() for _ in range(m)]
need_books = [input() for _ in range(n)]
for book in need_books:
    if book in my_books:
        print('YES')
    else:
        print('NO')
