import asyncio

# Создаем экземпляр события
event = asyncio.Event()


# Определяем корутину для ожидания события
async def wait_for_event():
    print("Ждём события")
    # Ожидаем событие
    await event.wait()
    print("Событие получено")


# Определяем корутину для установки события
async def set_event():
    print("Установка события")
    # Устанавливаем событие
    event.set()


async def main():
    task1 = asyncio.create_task(wait_for_event())
    task2 = asyncio.create_task(set_event())
    await asyncio.gather(task1, task2)


asyncio.run(main())
