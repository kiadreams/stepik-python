import os


def get_only_dirs(path: str) -> None:
    list_of_dirs = [
        e for e in sorted(os.listdir(path))
        if os.extsep not in e
    ]
    print(*list_of_dirs, sep='\n')
    print(len(list_of_dirs))


if __name__ == '__main__':
    path = os.path.abspath('../../')
    # print(path)
    get_only_dirs(path)
