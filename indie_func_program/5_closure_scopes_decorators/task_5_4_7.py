def print_goods(data):
    goods = [good.split(':') for good in data]
    sort_goods = sorted(goods, key=lambda x: (-float(x[1]), x[0].upper()))
    for name, price in sort_goods:
        print(f'{float(price):.2f} - {name}')


data1 = [
    'Sony PlayStation 5: 46000',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Смартфон Samsung Galaxy A11: 10000',
    'Планшет Samsung Galaxy Tab S6: 26600',
]
print_goods(data1)

