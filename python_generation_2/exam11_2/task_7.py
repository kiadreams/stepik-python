purchases = {}

for _ in range(int(input())):
    name, product, quantity = input().split()
    person = purchases.setdefault(name, {})
    person[product] = person.get(product, 0) + int(quantity)

for name, products in sorted(purchases.items()):
    print(f'{name}:')
    for product, quantity in sorted(products.items()):
        print(f'{product} {quantity}')
    