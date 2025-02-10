import asyncio


# Пример кода task.cancelled():
async def main_task():
    print("Корутина main_task запустилась")
    await asyncio.sleep(5)
    print("Корутина main_task завершилась")


async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()  # Отмена задачи
    await asyncio.sleep(2)
    if task.cancelled():  # Проверка, была ли задача отменена
        print(f"Задача отменена - {task.cancelled()}")


asyncio.run(main())
