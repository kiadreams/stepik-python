import os
import shutil
from datetime import datetime, timedelta


dt = datetime(2018, 1, 1)
td = timedelta(days=1)
while dt <= datetime(2025, 12, 31):
    year, d = str(dt.year), dt.strftime('%d')
    month, m = dt.strftime('%B'), dt.strftime('%b')
    os.makedirs(f'sales_{year}/{month}_{year[2:]}/{d}_{m}_{year[2:]}')
    dt += td


if __name__ == '__main__':
    for i in range(18, 26):
        if os.path.exists(f"sales_20{i}"):
            shutil.rmtree(f"sales_20{i}")
