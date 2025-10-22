import os
import stat


def get_permissions(path):
    return stat.filemode(os.stat(path).st_mode)


def change_permissions(path: str, mode: int) -> None:
    os.chmod(path, int(str(mode), base=8))


if __name__ == '__main__':
    file_name = 'hello.txt'
    print(get_permissions(file_name))
    change_permissions(file_name, 111)
    print(get_permissions(file_name))
    change_permissions(file_name, 666)
    print(get_permissions(file_name))