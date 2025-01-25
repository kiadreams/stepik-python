import asyncio
import time


async def coro(delay):
    await asyncio.sleep(delay)
    print(f"{delay=} Задача выполнена за {time.perf_counter() - start:.3f}")
    return delay


async def coro_a(delay):
    await asyncio.sleep(delay)
    print(
        f"{delay=} Другая задача выполнена за {time.perf_counter() - start:.3f}"
    )
    return delay


async def main(max_time=5):
    delays = [2, 3, 4, 5, 6, 7, 1, 8, 9]
    try:
        tasks = [
            asyncio.wait_for(
                asyncio.create_task(coro(value)), timeout=max_time
            )
            for value in delays
        ]
        # Доп задача, которую отправим в тот же gather()
        another_task = asyncio.create_task(coro_a(6))
        result = await asyncio.gather(*tasks, another_task)
        # ----можно убедиться, что все задачи продолжат выполнение и TimeoutError вызовут все "долгие" задачи с wait_for-----
        # result = await asyncio.gather(*tasks, another_task, return_exceptions=True)
        print(result)
    except asyncio.TimeoutError:
        print(f"TimeoutError: {time.perf_counter() - start:.3f}")
    # Несмотря на то, что работа gather() была остановлена, остальные задачи продолжат выполнение
    await asyncio.sleep(2)


start = time.perf_counter()
asyncio.run(main())
