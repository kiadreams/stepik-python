"""
При использовании asyncio.Lock() необходимо убедиться, что блокировка всегда освобождается, иначе
это может привести к блокировке всего приложения. Для этого можно использовать конструкцию
try/finally или async with.
"""

import asyncio

# Создание объекта Lock
lock = asyncio.Lock()


async def my_task(task_id):
    print(f"Задача {task_id} ожидает блокировки с помощью Lock")
    # Ожидание получения блокировки
    await lock.acquire()
    try:
        print(f"Задача {task_id} получила блокировку")
        await asyncio.sleep(2)

    finally:
        print(f"Задача {task_id} блокировка снята")
        # Освобождение блокировки
        lock.release()


async def main():
    tasks = [asyncio.create_task(my_task(i)) for i in range(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())
