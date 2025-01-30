import asyncio

async def my_task(n, loop):
    print(f"Задача {n} с идентификатором цикла {id(loop)} начинается")
    await asyncio.sleep(1)
    print(f"Задача {n} завершена")

async def main(loop):
    tasks = [my_task(i, loop) for i in range(5)]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    # Передача цикла событий в функцию main
    loop.run_until_complete(main(loop))
finally:
    print('Закрываем цикл событий')
    loop.close()