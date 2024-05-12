import asyncio


async def read_book(student: str, time: int) -> None:
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main2() -> None:
    alex_reading = asyncio.create_task(read_book("Алекс", 5))
    maria_reading = asyncio.create_task(read_book("Мария", 3))
    ivan_reading = asyncio.create_task(read_book("Иван", 4))
    await alex_reading
    await maria_reading
    await ivan_reading


async def main1() -> None:
    alex_reading = asyncio.create_task(read_book("Алекс", 5))
    maria_reading = asyncio.create_task(read_book("Мария", 3))
    ivan_reading = asyncio.create_task(read_book("Иван", 4))
    await asyncio.gather(alex_reading, maria_reading, ivan_reading)


async def main() -> None:
    await asyncio.gather(
        asyncio.create_task(read_book("Алекс", 5)),
        asyncio.create_task(read_book("Мария", 3)),
        asyncio.create_task(read_book("Иван", 4)),
    )


asyncio.run(main())
