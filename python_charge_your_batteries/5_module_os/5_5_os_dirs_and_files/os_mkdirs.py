import os
import stat


if os.path.exists('music/placebo'):
    os.removedirs('music/placebo')

dir_path = 'music/placebo'
os.makedirs(dir_path, 0o000, exist_ok=True)

print(stat.filemode(os.stat('music').st_mode))
print(stat.filemode(os.stat('music/placebo').st_mode))

os.chmod('music/placebo', 0o744)

print(stat.filemode(os.stat('music').st_mode))
print(stat.filemode(os.stat('music/placebo').st_mode))
