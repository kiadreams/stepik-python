import asyncio


async def coro(name: int, delay: int):
    print(f'Первое сообщение от корутины {name}')
    await asyncio.sleep(delay)
    print(f'Второе сообщение от корутины {name}')


async def main():
    tasks = [
        asyncio.create_task(coro(name, delay))
        for name, delay in enumerate([3, 2, 1], 1)
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
