import os

dir_name = 'report_'

for i in range(1, 11):
    os.mkdir(dir_name + str(i))

if __name__ == '__main__':
    for i in range(1, 11):
        name = dir_name + str(i)
        if os.path.exists(name):
            os.rmdir(name)
