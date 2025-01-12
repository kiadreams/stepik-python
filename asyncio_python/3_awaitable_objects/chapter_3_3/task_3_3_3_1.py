import asyncio


counters = {
    'Counter 1': 0,
    'Counter 2': 0
}

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}


async def counter(counter_name: str):
    while counters[counter_name] < max_counts[counter_name]:
        counters[counter_name] += 1
        await asyncio.sleep(1)
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [
        asyncio.create_task(counter(n)) for n in ('Counter 1', 'Counter 2')
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
