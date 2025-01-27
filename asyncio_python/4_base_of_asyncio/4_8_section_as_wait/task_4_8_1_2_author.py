import asyncio


processors_delays = {
    "Intel Core i9-11900K": 7.01,
    "Intel Core i7-11700K": 4.32,
    "Intel Core i5-11600K": 8.59,
    "AMD Ryzen 9 5950X": 2.53,
}

"""
Прибивание оставшихся задач, конкретно в этом примере, не обязательно,
т.к. await asyncio.wait -  была бы последней инструкцией в main(), и все задачи
все равно были бы остановлены по факту завершения работы цикла событий. Но вот
если бы после этой строки было бы еще какое-то ожидание, то мы увидели бы
плоды работы других задач.
"""


async def simulate_processing(delay):
    print(
        await asyncio.sleep(
            delay,
            f"Первый завершенный процесс: {asyncio.current_task().get_name()}",
        ),
    )


async def main():
    tasks = [
        asyncio.create_task(simulate_processing(delay), name=name)
        for name, delay in processors_delays.items()
    ]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED,
    )
    [task.cancel() for task in pending]
    print(pending)


asyncio.run(main())
