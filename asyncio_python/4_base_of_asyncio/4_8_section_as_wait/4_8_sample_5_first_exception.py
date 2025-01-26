import asyncio


async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)
    raise Exception("Ошибка в foo")


async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)
    raise Exception("Ошибка в bar")


async def main():
    tasks = [
        asyncio.create_task(foo(), name="foo"),
        asyncio.create_task(bar(), name="bar"),
    ]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_EXCEPTION
    )

    for task in done:
        print("Задание завершено:", task.get_name())
        if task.exception() is not None:
            print("Исключение задачи:", task.exception())
    for task in pending:
        print("Задача в ожидании:", task.get_name())


asyncio.run(main())
