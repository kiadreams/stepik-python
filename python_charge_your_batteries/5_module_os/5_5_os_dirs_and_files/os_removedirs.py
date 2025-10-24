import os

if os.path.exists('movies/comedy'):
    os.removedirs("movies/comedy")

if os.path.exists('musics'):
    os.rmdir('musics')

os.makedirs('movies/comedy')
os.mkdir('musics')
print(os.listdir())

# удаляем 'movies'
os.removedirs('movies/comedy')
print(os.listdir())
