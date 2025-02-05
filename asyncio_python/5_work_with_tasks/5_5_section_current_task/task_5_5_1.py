import asyncio


async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())


async def main():
    tasks = [process_task() for _ in range(10)]
    return await asyncio.gather(*tasks)


asyncio.run(main())
