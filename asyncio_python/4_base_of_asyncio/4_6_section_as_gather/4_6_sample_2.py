import asyncio

# При использовании значения return_exceptions=False по умолчанию, любая
# ошибка возникшая в корутине будет проброшена в основной код. При этом
# важно помнить, что задачи, в которых не возникло исключение, не отменяются,
# а продолжают свое выполнение


# В случае return_exceptions=True для тех корутин, которые завершились с
# ошибкой, в значение результата будет записана возникшая ошибка

async def my_coro(num):
    print(f"Корутина {num} началась")
    await asyncio.sleep(num)
    if num % 2 == 0:
        raise Exception(f"Ошибка в корутине {num}")
    print(f"Корутина {num} закончилась")
    return num


async def main():
    coros = [my_coro(i) for i in range(1, 6)]
    results = await asyncio.gather(*coros, return_exceptions=True)
    print(f'{results = }')


asyncio.run(main())
