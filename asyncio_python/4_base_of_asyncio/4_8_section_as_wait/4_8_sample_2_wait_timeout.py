import asyncio


async def my_coro(delay):
    """Асинхронная задача, которая просто ждет указанное время."""
    task_name = asyncio.current_task().get_name()
    print(f"{task_name} началась, будет выполняться {delay} секунд(ы).")
    await asyncio.sleep(delay)
    print(f"{task_name} завершена.")
    return f"{task_name}: результат"


async def main():
    tasks = [
        asyncio.create_task(my_coro(i), name=f"Задача_{i}")
        for i in range(1, 4)
    ]
    print("Запуск задач...")
    done, pending = await asyncio.wait(tasks, timeout=2)

    # Проверяем, какие задачи выполнены, а какие еще в ожидании
    print(f"\nРезультаты завершенных задач: {[d.result() for d in done]}")
    if pending:
        print(f"Ожидающие задачи: {[x.get_name() for x in pending]}")
        # Опционально: Можно отменить оставшиеся задачи, если это необходимо
        print(f"Отмена задач...")
        for task in pending:
            if task.get_name() == 'Задача_3':
                print(await task)
            else:
                print(f"{task.get_name()}: Отмена ")
                task.cancel()

    else:
        print(f"Все задачи завершены.")


asyncio.run(main())
