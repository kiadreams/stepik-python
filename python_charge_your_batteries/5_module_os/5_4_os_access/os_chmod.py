import os
import stat

filename = 'hello.txt'

mode = os.stat(filename).st_mode
print(stat.filemode(mode))
print()

print('Меняем разрешения на 777 (в Windows не всегда работает...)')
os.chmod(filename, 0o111)
mode = os.stat(filename).st_mode
print(stat.filemode(mode))

print('Меняем разрешения на 777 (в Windows просто так не работает...)')
os.chmod(filename, 0o666)
mode = os.stat(filename).st_mode
print(stat.filemode(mode))
