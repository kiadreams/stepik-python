import os
from datetime import datetime

for i in range(18, 26):
    for j in range(1, 13):
        month = datetime(1, j, 1).strftime("%B")
        os.makedirs(f'sales_20{i}/{month}_{i}')


if __name__ == '__main__':
    for i in range(18, 26):
        for j in range(1, 13):
            month = datetime(1, j, 1).strftime('%B')
            os.removedirs(f"sales_20{i}/{month}_{i}")
