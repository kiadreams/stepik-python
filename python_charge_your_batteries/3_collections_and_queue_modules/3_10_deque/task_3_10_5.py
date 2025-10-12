from collections import deque


class TextEditor:

    def __init__(self):
        self.text = []
        self.history = deque(maxlen=2)

    def add_text(self, text):
        self.text.append(text)

    def undo(self):
        if self.text:
            self.history.append(self.text.pop())

    def redo(self):
        if self.history:
            self.text.append(self.history.pop())

    def get_text(self):
        return ''.join(self.text)


editor = TextEditor()
editor.add_text("Hello, ")
assert editor.get_text() == "Hello, "

editor.add_text("World!")
assert editor.get_text() == "Hello, World!"

editor.add_text(" How are you!")
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.redo()
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.undo()
assert editor.get_text() == "Hello, "

print(editor.history)
