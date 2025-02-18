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
        [group.create_task(coro(), name=f"Задача_0{i}") for i in range(1, 4)]

    # Ожидание, пока все задачи не будут завершены...
    print("Все задачи были выполнены!")


asyncio.run(main())
