from typing import Any


# Напишите определение класса Stack
class EmptyStackError(BaseException):
    pass


class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()
        raise EmptyStackError

    def peek(self) -> Any:
        if self.stack:
            return self.stack[-1]
        raise EmptyStackError

    def is_empty(self) -> bool:
        return not self.stack

    @property
    def size(self) -> int:
        return len(self.stack)


# Проверки стека
my_stack = Stack()
assert my_stack.size == 0
assert my_stack.is_empty()
my_stack.push('A')
my_stack.push('W')
my_stack.push('M')
assert my_stack.size == 3
assert not my_stack.is_empty()
assert my_stack.pop() == 'M'

assert my_stack.peek() == 'W'
assert my_stack.pop() == 'W'

assert my_stack.peek() == 'A'
my_stack.push('hello')
assert my_stack.size == 2

assert my_stack.pop() == 'hello'
assert my_stack.pop() == 'A'
assert my_stack.is_empty()

try:
    my_stack.pop()
except EmptyStackError:
    pass