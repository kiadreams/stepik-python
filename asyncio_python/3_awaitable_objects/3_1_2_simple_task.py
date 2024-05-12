import asyncio
import time


# Объявление корутины.
async def coro(num: int, seconds: int) -> None:
    print(f"Задача{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"Задача{num} выполнена за {seconds} секунду(ы)")


async def main() -> None:
    # Создание задач из корутины.
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))
    # Происходит асинхронный запуск и ожидание выполнения задач.
    await task1
    await task2


start = time.time()
asyncio.run(main())
print(f"Программа выполнена за {time.time() - start:.3f} секунд(ы)")
