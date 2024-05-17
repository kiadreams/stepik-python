# Напишите определение класса File
class File:

    def __init__(self, size_in_bytes):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B"
        elif 1024 <= self._size_in_bytes < 1024 ** 2:
            return f"{(self._size_in_bytes / 1024):0.2f} KB"
        elif 1024 ** 2 <= self._size_in_bytes < 1024 ** 3:
            return f"{(self._size_in_bytes / 1024 ** 2):0.2f} MB"
        else:
            return f"{(self._size_in_bytes / 1024 ** 3):0.2f} GB"

    @size.setter
    def size(self, size):
        self._size_in_bytes = size

# Ниже код для проверки методов класса File

file = File(5)
assert file.size == "5 B"
file.size = 1023
assert file.size == "1023 B"
file.size = 1024
assert file.size == "1.00 KB"

file_1 = File(1500000)
assert file_1._size_in_bytes == 1500000
assert file_1.size == "1.43 MB"

file_2 = File(1500)
assert file_2.size == "1.46 KB"


file_3 = File(2789326322)
assert file_3.size == "2.60 GB"
file_3.size = 1073741824
assert file_3.size == "1.00 GB"

print('Good')