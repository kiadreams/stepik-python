import asyncio


async def task(number, first_lock, second_lock):
    print(f"Задача {number}: пытается захватить первую блокировку")
    async with first_lock:
        print(f"Задача {number}: захватила первую блокировку")
        await asyncio.sleep(1)  # Имитация работы в критическом участке
        print(f"Задача {number}: пытается захватить вторую блокировку")

        async with second_lock:
            print(f"Задача {number}: захватила вторую блокировку")
            # Дополнительная работа в критическом участке
            await asyncio.sleep(1)
    print(f"Задача {number}: завершила выполнение")


async def main():
    # Инициализация двух асинхронных блокировок
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()

    # Запуск корутин с блокировками в разном порядке
    await asyncio.gather(
        task(1, lock1, lock2),
        task(2, lock2, lock1),
    )


asyncio.run(main())
