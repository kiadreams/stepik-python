from collections import UserString


# Напишите определение класса StringDeque
class StringDeque(UserString):

    def append(self, symbol: str) -> None:
        self.__validate_symbol(symbol)
        self.data = self.data + symbol

    def appendleft(self, symbol: str) -> None:
        self.__validate_symbol(symbol)
        self.data = symbol + self.data

    @staticmethod
    def __validate_symbol(symbol: str) -> None:
        if not isinstance(symbol, str) or len(symbol) > 1:
            raise ValueError('Symbol must be a string')


# Проверки для класса StringDeque

deque = StringDeque("abc")

assert type(deque) == StringDeque
deque.appendleft("d")
assert deque.data == 'dabc'
deque.append("e")
assert deque.data == 'dabce'

try:
    deque.append(123)
except ValueError:
    pass

try:
    deque.append('hello')
except ValueError:
    pass

try:
    deque.append('')
except ValueError:
    pass

try:
    deque.appendleft([1])
except ValueError:
    pass

try:
    deque.appendleft('hi')
except ValueError:
    pass
