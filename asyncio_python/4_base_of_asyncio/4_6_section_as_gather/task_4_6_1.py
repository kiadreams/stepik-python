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
    await asyncio.sleep(0.1)
    if not book["Наличие на полке"]:
        return (
            f"{book["Порядковый номер"]}: "
            f"{book["Автор"]}: {book["Название"]} ({book["Год издания"]})"
        )
    return None


async def main():
    books = filter(
        lambda x: x is not None,
        await asyncio.gather(*map(check_book, books_json)),
    )
    print(*books, sep="\n")


asyncio.run(main())
