import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f"{name} начала свою работу!")
    await asyncio.sleep(1)
    print(f"{name} завершена!")


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        tasks = [group.create_task(coro(), name=f"Задача_0{i}") for i in range(1, 4)]
        await asyncio.sleep(0.5)
        # Отмена второй задачи
        tasks[1].cancel()
    # Проверка состояния каждой задачи
    for task in tasks:
        print(f"{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}")


asyncio.run(main())
