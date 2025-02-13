import asyncio


async def async_operation():
    print("Асинхронная операция началась...")
    await asyncio.sleep(2)
    print("Асинхронная операция завершена.")
    return "Результат асинхронной операции"


def on_completion(task):  # Callback-функция
    result = task.result()
    print(f"Callback функция вызвана. Получен результат: {result}")


async def main():
    task = asyncio.create_task(async_operation())
    task.add_done_callback(on_completion)  # Регистрация callback-функции
    await task


asyncio.run(main())
