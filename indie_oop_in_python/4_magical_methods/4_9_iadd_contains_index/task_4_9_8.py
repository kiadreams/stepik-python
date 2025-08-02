class SparseArray:

    def __init__(self, *args: int):
        self._data: list[int | None] = list(args)

    def __setitem__(self, index: int, value: int):
        self.__extend_array(index)
        self._data[index] = value

    def __getitem__(self, index: int) -> int | None:
        self.__extend_array(index)
        return self._data[index]

    def __delitem__(self, index: int) -> None:
        if index < len(self._data):
            self._data[index] = None

    def __extend_array(self, index: int) -> None:
        if index >= len(self._data):
            self._data += [None] * (index - len(self._data) + 1)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def values(self) -> tuple[int | None, ...]:
        return tuple(self._data)


# Проверка работы кода--------------------------------------------------------
array = SparseArray(1, 2, 3)
print(array.values)
print(array[7])
print(array.values)
array[6] = 100
print(array.values)
array[10] = 200
print(array.values)
del array[1]
print(array.values)
print(len(array))
del array[100]
print(array.values)
