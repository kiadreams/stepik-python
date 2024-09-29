from unicodedata import category


def is_table_free(n):
    return tables.get(n) is None


def reserve_table(n, name, vip_status=False):
    if is_table_free(n):
        tables[n] = {"name": name, "is_vip": vip_status, "order": {}}


def make_order(number, **kwargs):
    all_category = {'salad', 'soup', 'main_dish', 'drink', 'desert'}
    orders = {k: v for k, v in kwargs.items() if k in all_category}
    if tables.get(number) is not None:
        tables[number]["order"].update(orders)


tables = {
    1: {"name": "Andrey", "is_vip": True, "order": {}},
    2: None,
    3: None,
    4: None,
    5: {"name": "Vasiliy", "is_vip": False, "order": {}},
}

make_order(1, soup='Borsh')
make_order(1, desert='Наполеон', drink='Чай')
print(tables)
