import csv


with open('4_2_work_with_csv/sales.csv', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=';')
    next(data)
    for product in data:
        name, old_price, new_price = product
        if int(old_price) > int(new_price):
            print(name)
