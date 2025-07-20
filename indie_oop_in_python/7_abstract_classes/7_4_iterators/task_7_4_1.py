class SequenceIterator:
    def __init__(self, container):
        self.container = container
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.container) and not self.index % 2:
            self.index = 1
        elif self.index >= len(self.container):
            raise StopIteration
        return self.container[self.index]


# Проверка работы-------------------------------------------------------------
cont = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
assert [i for i in cont] == [1, 4, 43, 'hello', 5, 6, True]
