import asyncio


async def task1() -> None:
    await asyncio.sleep(1)
    print("Привет из корутины task1")


async def task2() -> None:
    await asyncio.sleep(1)
    print("Привет из корутины task2")


async def main() -> None:
    await asyncio.create_task(task1())
    await asyncio.create_task(task2())


asyncio.run(main())
