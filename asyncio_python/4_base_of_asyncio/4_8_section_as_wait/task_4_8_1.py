import asyncio


# Полный словарь вшит в задачу
processors_delays = {
    "Intel Core i9-11900K": 7.01,
    "Intel Core i7-11700K": 4.32,
    "Intel Core i5-11600K": 8.59,
    "AMD Ryzen 9 5950X": 2.53,
}


async def simulate_processing(delay):
    task_name = await asyncio.sleep(delay, asyncio.current_task().get_name())
    print(f"Первый завершенный процесс: {task_name}")


async def main():
    tasks = [
        asyncio.create_task(simulate_processing(delay), name=name)
        for name, delay in processors_delays.items()
    ]
    done, _ = await asyncio.wait(tasks, return_when="FIRST_COMPLETED")


asyncio.run(main())
