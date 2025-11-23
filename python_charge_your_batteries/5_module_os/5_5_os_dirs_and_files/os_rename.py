import os


dist_dir = 'musics'

if os.path.exists(dist_dir):
    os.rmdir(dist_dir)

if os.path.exists('second.txt'):
    os.remove('second.txt')

source_dir = 'movies'
os.mkdir(source_dir, 0o774)
print(os.listdir())

# переименование 'movies' в 'musics'
os.rename(source_dir, dist_dir)
print(os.listdir())


with open('first.txt', 'w') as f:
    pass

print(os.listdir())

os.rename('first.txt', 'second.txt')
print(os.listdir())