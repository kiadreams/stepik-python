import asyncio

async def task_coroutine():
    print('Задача выполняется')
    await asyncio.sleep(1)

    # Возвращение значения (никогда не достигается)
    return 99


async def main():
    print('Основная корутина начата')
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)

    # Отмена задачи
    task.cancel()
    # Ожидание момента для отмены задачи
    await asyncio.sleep(0.1)
    try:
        # Получение результата
        value = task.result()
        print(f'Результат: {value}')
        # print(await task)
    except asyncio.CancelledError:
        print('Задача была отменена.')
    print('Основная корутина завершена')


asyncio.run(main())