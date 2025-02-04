import asyncio


# Это скрыто под капотом задачи
async def coroutine():
    await asyncio.sleep(0.1)
    raise Exception("Моя ошибка!")
    return 56


async def main():
    task = asyncio.create_task(coroutine())
    await asyncio.sleep(0.2)
    try:
        print(task.result())
    except Exception as e:
        print(e)


asyncio.run(main())
