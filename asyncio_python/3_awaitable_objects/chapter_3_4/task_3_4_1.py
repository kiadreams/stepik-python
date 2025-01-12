import asyncio


async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    task = asyncio.create_task(set_future_result('Успех', 2))
    check_status(task, 'до выполнения')
    print("Задача запущена, ожидаем завершения...")
    await task
    check_status(task, 'после выполнения')
    return task.result()


async def main():
    res = await create_and_use_future() # Вызовите и дождитесь необходимую функцию
    print("Результат из Task:", res)


def check_status(task, period):
    if task.done():
        print(f'Состояние Task {period}: Завершено')
    else:
        print(f'Состояние Task {period}: Ожидание')


asyncio.run(main())