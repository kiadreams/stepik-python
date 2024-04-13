import time
import asyncio


# Объявление корутинной функции(используется "async def")
async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание объектов корутин путем вызова корутинной функции.
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)
    # Запуск и ожидание выполнения объектов корутин.
    # print(type(coro1), coro1.__str__())
    # await coro2
    # await coro1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')
