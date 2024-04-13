def read_csv():
    with open('17_3_files/data.csv', encoding='utf-8') as f:
        keys = f.readline().rstrip().split(',')
        lines = [l.rstrip().split(',') for l in f.readlines()]
        return [dict(zip(keys, line)) for line in lines]


print(read_csv())