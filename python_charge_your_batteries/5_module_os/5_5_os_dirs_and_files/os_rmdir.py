import os


dir_movie = 'movies'
dist_music = 'musics'

if os.path.exists(dir_movie):
    os.rmdir(dir_movie)

if os.path.exists(dist_music):
    os.rmdir(dist_music)

os.mkdir(dir_movie)
os.mkdir(dist_music)
print(os.listdir())

# удаляем 'movies'
os.rmdir(dir_movie)
print(os.listdir())
