import asyncio


async def my_task(number):
    # Получение текущего объекта задачи asyncio.
    current_task = asyncio.current_task()

    # Вывод информации о старте задачи и объекте задачи.
    print(f"Текущий объект задачи: {current_task}")
    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(my_task(1))
    await asyncio.gather(task1)


asyncio.run(main())
