import os
import time
import stat

filename = __file__

stat_info = os.stat(filename)

print(f'File: {filename}')
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created      :', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))
print()

print(f'File: {filename}')
print('Permissions:', oct(stat_info.st_mode))
print('Permissions:', stat_info.st_mode)
print('Permissions:', stat.filemode(stat_info.st_mode))
