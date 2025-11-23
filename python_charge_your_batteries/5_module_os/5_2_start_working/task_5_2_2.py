import os


class FileCount:

    def __get__(self, instance, owner):
        print(f'self: {self}, instance: {instance}, owner: {owner}')
        if instance is None:
            return self
        return len(os.listdir(instance.path))


class Folder:
    count = FileCount()

    def __init__(self, path: str):
        self.path = '/'.join([os.getcwd(), path])


# проверки для класса Folder

folder_include = Folder('')
print(folder_include.count)
assert folder_include.count == 2

folder_nested = Folder('nested')
assert folder_nested.count == 3

print('Good')
