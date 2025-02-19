import asyncio

"""
Асинхронные блокировки и семафоры: если вы используете асинхронные примитивы синхронизации, такие 
как блокировки или семафоры, async with может помочь корректно захватывать и освобождать эти 
примитивы, предотвращая возможные проблемы с синхронизацией.
"""


async def protected_section(lock, task_id):
    # Используем async with для корректного захвата и освобождения блокировки
    async with lock:
        print(f"Task {task_id} has entered the protected section")
        await asyncio.sleep(1)
        print(f"Task {task_id} has left the protected section")


async def main():
    lock = asyncio.Lock()
    tasks = [protected_section(lock, i) for i in range(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())
