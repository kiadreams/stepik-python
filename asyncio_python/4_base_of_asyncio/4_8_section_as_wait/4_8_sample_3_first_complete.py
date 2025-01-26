import asyncio


async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)


async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)


async def main():
    tasks = [
        asyncio.create_task(foo(), name="foo"),
        asyncio.create_task(bar(), name="bar"),
    ]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )

    for task in done:
        print("Задание завершено:", task.get_name())
    for task in pending:
        print("Задание ожидает выполнения:", task.get_name())


asyncio.run(main())
