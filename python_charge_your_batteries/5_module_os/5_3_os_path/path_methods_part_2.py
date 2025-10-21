import os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/']

print('PREFIX:', os.path.commonprefix(paths))
print('PREFIX:', os.path.commonprefix(['/usr/documents/', '/usr/docs/reports']))
print('PREFIX:', os.path.commonprefix(['/usr/documents/', '/home/docs']))
print('PREFIX:', os.path.commonprefix(['/usr/documents/', 'home/docs']))
print()

print('PREFIX:', os.path.commonpath(paths))
print('PREFIX:', os.path.commonpath(['/usr/documents/', '/usr/docs/reports']))
print('PREFIX:', os.path.commonpath(['/usr/documents/', '/home/docs']))
print()

#Но будьте аккуратны, если последовательность paths содержит как абсолютные,
# так и относительные пути, то возникнет исключение.
#ValueError: Can't mix absolute and relative paths

# print('PREFIX:', os.path.commonpath(paths))
# print('PREFIX:', os.path.commonpath(['/usr/documents/', 'home/docs']))
print()

print(os.path.join('home', 'user', 'egoroff'))
paths_2 = ('one', 'two', 'three')
print(os.path.join(*paths_2))
print()

PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

for path in PATHS:
    print(f'{path:21} : {os.path.normpath(path)}')
print()

paths = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in paths:
    print(f'{path:17} : {os.path.abspath(path)}')
print()


dir_path = '../' + os.path.basename(os.getcwd())
print(os.getcwd(), dir_path)


file_path = 'path_methods_part_2.py'
if os.path.isfile(file_path):
    print(f"{file_path} это файл.")
else:
    print(f"{file_path} это не файл.")


if os.path.isdir(dir_path):
    print(f"{dir_path} is a directory.")
else:
    print(f"{dir_path} is not a directory.")
