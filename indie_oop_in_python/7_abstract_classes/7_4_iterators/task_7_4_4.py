class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __iter__(self):
        # тут определите, что будете передавать итератору
        return LibraryIterator(self.books)


class LibraryIterator:
    def __init__(self, books: list[Book]):
        self.books = books
        self.b_index = 0
        self.p_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.p_index >= len(self.books[self.b_index].pages):
            self.p_index = 0
            self.b_index += 1
        if self.b_index >= len(self.books):
            raise StopIteration
        page = self.books[self.b_index].pages[self.p_index]
        self.p_index += 1
        return page


# Проверка работы------------------------------------------------------------
# Пример использования
book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Используем вложенный итератор для обхода страниц в библиотеке
for p in library:
    print(p)
