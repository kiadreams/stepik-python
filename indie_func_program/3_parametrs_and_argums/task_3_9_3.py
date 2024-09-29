all_category = {'salad', 'soup', 'main_dish', 'drink', 'desert'}


def is_table_free(n):
    return tables.get(n) is None


def reserve_table(n, name, vip_status=False):
    if is_table_free(n):
        tables[n] = {"name": name, "is_vip": vip_status, "order": {}}


def make_order(number, **kwargs):
    orders = {k: v for k, v in kwargs.items() if k in all_category}
    if tables.get(number) is not None:
        tables[number]["order"].update(orders)


def delete_order(*, number_table, delete_all=False, **kwargs):
    order = tables[number_table]['order']
    if delete_all:
        order.clear()
    else:
        for k, v in kwargs.items():
            if k in order and v:
                order.pop(k)


# ПРОВЕРКА КОДА!!!
tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, delete_all=True)
print(tables)