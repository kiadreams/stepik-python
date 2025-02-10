import asyncio


"""
Использование этого метода в пользовательском коде не рекомендуется, и этот пример предоставлен 
только для демонстрации механизма. В обычной практике разработки достаточно использовать методы 
cancel() и cancelled() для управления отменой задач и проверки их состояния соответственно.
"""


# Пример кода task.cancelling():
async def long_running_task():
    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        # Обработка отмены задачи и вывод сообщения при перехвате asyncio.CancelledError
        print("Получена команда на отмену задачи task")
        # Подъем перехваченного ранее исключения, для срабатывания логики в main().
        raise


async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(0.5)
    print(f"Количество запросов на отмену задачи: {task.cancelling()}")
    # Отменяем задачу
    print("Отменяем задачу...")
    task.cancel()

    # Используем cancelling() для проверки, была ли задача помечена для отмены
    if task.cancelling() > 0:
        print(f"Количество запросов на отмену задачи: {task.cancelling()}")
        print("Дана команда отмены задачи task")
    else:
        print("Задача task не ожидает отмены")
    # Перехват исключения asyncio.CancelledError в main()
    try:
        await task
    except asyncio.CancelledError:
        print(f"Задача task отменена: {task.cancelled()}")


asyncio.run(main())
