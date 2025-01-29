import asyncio
import random


async def some_task(num):
    await asyncio.sleep(delay := random.random())
    return f'Task {num} completed, {delay=:.3f}'


async def main():
    tasks = [asyncio.create_task(some_task(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)
    for task in tasks:
        if task.done():
            print(await task)


asyncio.run(main())
