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
    num, author, name, publication, presence = book.values()
    (
        print(f"{num}: {author}: {name} ({publication})")
        if await asyncio.sleep(0.1, not presence)
        else ...
    )


async def main():
    await asyncio.gather(*[check_book(x) for x in books_json])


asyncio.run(main())
