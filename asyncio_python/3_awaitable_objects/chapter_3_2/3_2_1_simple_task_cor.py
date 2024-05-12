import asyncio
import time


async def generate(number: int) -> None:
    print(f"Корутина generate с аргументом {number} стартовала...")
    await asyncio.sleep(1)
    print(f"Корутина generate с аргументом {number} финишировала!")


async def main() -> None:
    await asyncio.gather(*[generate(itr) for itr in range(10)])


async def main2() -> None:
    for itr in range(10):
        await generate(itr)


asyncio.run(main2())
