book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]
book = [1, 'Балакирев С.М.', 'Python', 2100.0]
# book = [1, 'Балакирев С.М.', 'Python', 2023]
# t = (int, str, str, float, int)
# book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case _, author, title if len(author) > 5 and len(title) > 9:
        print('Yes', 1)
    case _, author, title, float() as price if len(author) > 5 and price > 0:
        print('Yes', 2)
    case _, author, title, int() as year if year > 2019:
        print('Yes', 3)
    case _, author, title, price, year if price > 0 and year > 2019:
        print('Yes', 4)
    case _:
        print('No')
