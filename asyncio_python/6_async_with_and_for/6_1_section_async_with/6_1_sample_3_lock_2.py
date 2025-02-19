import asyncio


async def protected_section_1(lock):
    # Используем async with для корректного захвата и освобождения блокировки
    async with lock:
        task_id = asyncio.current_task().get_name()
        print(f"Task {task_id} has entered the protected section 1")
        await asyncio.sleep(1)
        print(f"Task {task_id} has left the protected section 1")


async def protected_section_2(lock):
    # Используем async with для корректного захвата и освобождения блокировки
    async with lock:
        task_id = asyncio.current_task().get_name()
        print(f"Task {task_id} has entered the protected section 2")
        await asyncio.sleep(1)
        print(f"Task {task_id} has left the protected section 2")


async def main():
    lock = asyncio.Lock()
    tasks_1 = [asyncio.create_task(protected_section_1(lock)) for _ in range(3)]
    tasks_2 = [asyncio.create_task(protected_section_2(lock)) for _ in range(3)]
    await asyncio.gather(*(tasks_1 + tasks_2))


asyncio.run(main())
