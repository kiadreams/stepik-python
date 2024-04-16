import csv


with open('4_2_work_with_csv/products.csv', encoding='utf-8') as f:
    rows = csv.reader(f)
    print(*rows, sep='\n')

print()

with open('4_2_work_with_csv/products.csv', encoding='utf-8') as f2:
    rows = csv.DictReader(f2)
    print(next(rows))
