all_category = {'salad', 'soup', 'main_dish', 'drink', 'desert'}


def is_table_free(n):
    return tables.get(n) is None


def reserve_table(n, name, vip_status=False):
    if is_table_free(n):
        tables[n] = {"name": name, "is_vip": vip_status, "order": {}}


def make_order(number, **kwargs):
    orders = {
        k: v.split(',') for k, v in kwargs.items()
        if k in all_category
    }
    if tables.get(number) is not None:
        for c, dishes in orders.items():
            tables[number]["order"].setdefault(c, []).extend(dishes)


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
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь,Мимоза', breakfast='Яичница,Бекон')
make_order(2, drink='Raf,Coffee,Juice', main_dish='Утка по-пекински,Отбивная')
make_order(2, desert='Трюфель', call='такси')

make_order(1, desert='Наполеон', drink='Чай', meal='Манка,Овсянка')
make_order(1, desert='Вишня', drink='Кофе')
print(tables)
delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)