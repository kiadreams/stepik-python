import asyncio


# Это скрыто под капотом задачи
async def coroutine():
    await asyncio.sleep(5)
    return 56


async def main():
    task = asyncio.create_task(coroutine())
    await task
    print(task.result())


asyncio.run(main())
