import asyncio


async def generate(number: int) -> None:
    print(f"Корутина generate с аргументом {number}")


async def main() -> None:
    await asyncio.gather(*[generate(itr) for itr in range(10)])


asyncio.run(main())
