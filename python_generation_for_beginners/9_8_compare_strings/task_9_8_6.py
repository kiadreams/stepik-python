books = []
for _ in range(int(input())):
    author, title = input().split(', ')
    last_name, _ = author.split()
    books.append((last_name, title))
print('YES' if books == sorted(books) else 'NO')