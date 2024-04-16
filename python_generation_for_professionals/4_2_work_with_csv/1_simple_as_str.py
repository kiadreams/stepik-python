with open('4_2_work_with_csv/products.csv', encoding='utf-8') as f:
    data = f.read()
    for line in data.splitlines():
        print(line.split(','))
