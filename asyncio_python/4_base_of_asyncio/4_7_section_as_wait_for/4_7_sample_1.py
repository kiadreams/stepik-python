import asyncio

async def long_running_task(delay):
    # Эмуляция долгой задачи
    if delay == 4:
        raise ValueError('ожидание равно 4 секунды')
    await asyncio.sleep(delay)
    return "Задача завершена"

async def main():
    # Создаем задачу
    task = asyncio.create_task(long_running_task(10))
    try:
        # Ожидаем завершения задачи в течение 5 секунд
        await asyncio.wait_for(task, timeout=5)
    except TimeoutError:
        print("Задача 1 не была завершена в установленное время")
    # Ожидаем завершения корутины за 5 секунд
    result = await asyncio.wait_for(long_running_task(3), 5)
    print(f'Задача 2: {result}')
    # Пуск несколько задач с asyncio.wait_for и с защитой от исключений
    result2 = await asyncio.gather(
        asyncio.wait_for(long_running_task(2), 5),
        asyncio.wait_for(long_running_task(4), 5),
        asyncio.wait_for(long_running_task(7), 5),
        return_exceptions=True,
    )
    print(result2)


asyncio.run(main())