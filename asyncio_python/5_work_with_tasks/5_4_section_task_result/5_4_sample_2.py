import asyncio


async def task_coroutine():
    print("Задача выполняется")
    await asyncio.sleep(1)

    # Возвращение значения (никогда не достигается)
    return 99


async def main():
    print("Основная корутина начата")
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)
    try:
        value = task.result()
        print(f"Результат: {value}")
    except asyncio.InvalidStateError:
        print("Получено исключение InvalidStateError")
    print("Основная корутина завершена")


asyncio.run(main())
