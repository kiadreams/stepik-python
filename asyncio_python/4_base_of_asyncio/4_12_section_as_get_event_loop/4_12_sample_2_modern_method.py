import asyncio

async def my_task(n):
    loop = asyncio.get_running_loop()  # Получение текущего цикла событий
    print(f"Задача {n} с идентификатором цикла {id(loop)} начинается")
    await asyncio.sleep(1)
    print(f"Задача {n} завершена")

async def main():
    tasks = [my_task(i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())