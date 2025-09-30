from typing import Any


# Напишите определение класса Queue
class Queue:

    def __init__(self) -> None:
        self.queue = []

    @property
    def size(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return not self.queue

    def enqueue(self, item) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)
        raise IndexError

    def peek(self) -> Any:
        if self.queue:
            return self.queue[0]
        raise IndexError


# Проверки очереди
my_queue = Queue()
assert my_queue.size == 0
assert my_queue.is_empty()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
assert my_queue.size == 3
assert not my_queue.is_empty()
assert my_queue.dequeue() == 1

assert my_queue.peek() == 2
assert my_queue.dequeue() == 2

assert my_queue.peek() == 3
my_queue.enqueue('hello')
assert my_queue.size == 2

assert my_queue.dequeue() == 3
assert my_queue.dequeue() == 'hello'
assert my_queue.is_empty()

try:
    my_queue.dequeue()
except IndexError:
    pass
