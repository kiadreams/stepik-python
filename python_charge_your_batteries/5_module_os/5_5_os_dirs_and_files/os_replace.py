import os

source_dir = 'movies_1'
dist_dir = 'musics_1'
if os.path.exists(dist_dir):
    os.rmdir(dist_dir)

os.mkdir(source_dir, 0o774)
print(os.listdir())

# переименование 'movies' в 'musics'
os.replace(source_dir, dist_dir)
print(os.listdir())
