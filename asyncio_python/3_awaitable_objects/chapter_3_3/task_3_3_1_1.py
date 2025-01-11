import asyncio


async def coro_1():
    await asyncio.sleep(1)
    print('Coroutine 1 is done')


async def coro_2():
    await asyncio.sleep(2)
    print('Coroutine 2 is done')


async def coro_3():
    await asyncio.sleep(3)
    print('Coroutine 3 is done')


async def main():
    tasks = [
        asyncio.create_task(coro_1()),
        asyncio.create_task(coro_2()),
        asyncio.create_task(coro_3()),
    ]
    # await asyncio.sleep(3)
    await asyncio.gather(*tasks)

asyncio.run(main())