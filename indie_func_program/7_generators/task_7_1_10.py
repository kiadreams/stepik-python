def chunker(_iterable, size):
    index = 0
    while chnk := _iterable[index : index + size]:
        yield chnk
        index += size


# Второй вариант
def chunker2(obj, part):
    yield from [obj[i : i + part] for i in range(0, len(obj), part)]


text = """Python 3.12 is the latest stable release of the Python programming language, with a mix of changes to the language and the standard library."""

for chunk in chunker(text, 7):
    print(chunk)

for chunk in chunker(range(56), 9):
    print(list(chunk))
