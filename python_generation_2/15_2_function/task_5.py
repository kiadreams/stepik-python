def print_products(*args):
    products = [p.capitalize() for p in args if type(p) == str and p.strip()]
    if not products:
        print('Нет продуктов')
    else:
        for ind, product in enumerate(products, 1):
            print(f'{ind}) {product}')


print_products([4], {}, 1, 2, {'Beegeek'}, '')
print()
print_products('Бананы', [1, 2], ('Stepik',),
               'Яблоки', '', 'макароны', 5, True)
