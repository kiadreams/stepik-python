import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn():
    print(
        f"Старт blocking_fn() в потоке c id {threading.current_thread().ident}"
        f" в {time.strftime('%X')}",
    )
    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(1)  # Имитация выполнения длительной операции.
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")


# Функция асинхронного sleep()
async def sleep_fn():
    print(
        f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в "
        f"{time.strftime('%X')}",
    )
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    print(
        f"Старт main в потоке c id {threading.current_thread().ident} в "
        f"{time.strftime('%X')}",
    )

    # Создание корутины, для запуска в независимом потоке
    coro = asyncio.to_thread(blocking_fn)
    print(f"Тип объекта coro: {type(coro)}")

    # Асинхронный запуск задач.
    await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f"Время выполнения программы: {(time.time() - start)}")
