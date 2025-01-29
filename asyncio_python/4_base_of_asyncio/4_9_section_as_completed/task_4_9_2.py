import asyncio
import random

# Не менять!
random.seed(1)


async def collect_gold():
    await asyncio.sleep(random.randint(1, 5))
    return random.randint(10, 50)


async def main():
    total = 0
    tasks = [asyncio.create_task(collect_gold()) for _ in range(10)]
    for task in asyncio.as_completed(tasks):
        amount = await task
        total += amount
        print(f"Собрано {amount} единиц золота.")
        print(f"Общее количество золота: {total} единиц.\n")


asyncio.run(main())
