import os
import stat


dir_name = "new_folder"

if os.path.exists(dir_name):
    os.chmod(dir_name, 0o777)
    os.rmdir(dir_name)


os.mkdir(dir_name, mode=0o111)

mode = os.stat(dir_name).st_mode
print(stat.filemode(mode), mode, oct(mode))

os.chmod(dir_name, 0o000)

mode = os.stat(dir_name).st_mode
print(stat.filemode(mode))
