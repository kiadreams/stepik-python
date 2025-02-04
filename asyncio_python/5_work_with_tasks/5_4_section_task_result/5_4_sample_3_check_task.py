import asyncio


async def task_coroutine():
    print("Задача выполняется")
    await asyncio.sleep(1)
    return 99


async def main():
    print("Основная корутина начата")
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)

    # Проверка, завершена ли задача
    if task.done():
        value = task.result()  # Получение результата завершённой задачи
        print(f"Результат: {value}")
    else:
        print("Задача еще не завершена")

    print("Основная корутина завершена")


asyncio.run(main())
