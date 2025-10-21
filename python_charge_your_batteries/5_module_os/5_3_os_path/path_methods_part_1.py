import os

print(os.sep)
print(os.extsep)
print(os.pardir)
print(os.curdir)
print()

print(os.path.split(os.getcwd()))
print()

PATHS = [
    '/usr/egoroff/start.py',
    '/usr/egoroff/',
    '/usr/egoroff',
    '../usr/',
    '../usr',
    'usr',
    '/',
    '.',
    '',
]

for path in PATHS:
    print(f'{path:21} : {os.path.split(path)}')
print()

for path in PATHS:
    print(f'{path:21} : {os.path.basename(path)}')
print()

for path in PATHS:
    print(f'{path:21} : {os.path.dirname(path)}')
print()

for path in PATHS:
    print(f'{path:21} : {os.path.splitext(path)}')
