import asyncio


books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True,
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False,
    },
]


async def check_book(book):
    num, author, title, year, is_on_shelf = book.values()
    if await asyncio.sleep(0.1, not is_on_shelf):
        return f"{num}: {author}: {title} ({year})"
    return None


async def main():
    books = filter(
        lambda x: x is not None,
        await asyncio.gather(*map(check_book, books_json)),
    )
    print(*books, sep="\n")


asyncio.run(main())
