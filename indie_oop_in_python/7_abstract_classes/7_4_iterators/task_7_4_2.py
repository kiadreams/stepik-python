class StackIterator:
    def __init__(self, stack: 'Stack'):
        self.stack = stack.items
        self.index = len(self.stack)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index:
            self.index -= 1
            return self.stack[self.index]
        raise StopIteration


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return StackIterator(self)



# Проверка работы-------------------------------------------------------------
stack = Stack()

stack.push(100)
stack.push(True)
stack.push('hello')
stack.push('world')

# Используем итератор для обхода стека
assert [i for i in stack] == ['world', 'hello', True, 100]
