import asyncio


counters = {'Counter 1': 0, 'Counter 2': 0, 'Counter 3': 0}
max_counts = {'Counter 1': 10, 'Counter 2': 5, 'Counter 3': 15}
delays = {'Counter 1': 1, 'Counter 2': 2, 'Counter 3': 0.5}


async def counter(counter_name: str):
    while counters[counter_name] < max_counts[counter_name]:
        counters[counter_name] += 1
        await asyncio.sleep(delays[counter_name])
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [
        asyncio.create_task(counter(n))
        for n in ('Counter 1', 'Counter 2', 'Counter 3')
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
