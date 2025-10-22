import os
import stat


def get_permissions(path: str) -> str:
    return stat.filemode(os.stat(path).st_mode)[1:]


if __name__ == '__main__':
    print(get_permissions(__file__))