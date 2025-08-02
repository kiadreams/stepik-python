class FibonacciIterator:
    def __init__(self, n: int) -> None:
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self) -> 'FibonacciIterator':
        return self

    def __next__(self) -> int:
        if self.n:
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            self.n -= 1
            return current
        raise StopIteration


# Проверка работы-------------------------------------------------------------
fibonacci_iter = FibonacciIterator(7)
assert [i for i in fibonacci_iter] == [0, 1, 1, 2, 3, 5, 8]
