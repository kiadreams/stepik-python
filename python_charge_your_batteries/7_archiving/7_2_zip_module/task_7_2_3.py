import os
from zipfile import ZipFile


if os.path.exists('numbers.zip'):
    os.remove('numbers.zip')

with ZipFile('numbers.zip', 'a') as z:
    for i in range(10):
        z.writestr(f'number_{i}.txt', f'This is number {i}')

with ZipFile('numbers.zip', 'a') as z:
    z.printdir()