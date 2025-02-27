import asyncio


robot_names = ["Электра", "Механикс", "Оптимус", "Симулакр", "Футуриус"]
lock = asyncio.Lock()
count = 0


async def move(robot):
    global count

    # print(f"Робот {robot} передвигается к месту A")
    # count += 1
    # await asyncio.sleep(1)
    # print(f'Робот {robot} достиг места A. Место A посещено {count} раз')

    async with lock:
        print(f"Робот {robot} передвигается к месту A")
        count += 1
        await asyncio.sleep(1)
        print(f'Робот {robot} достиг места A. Место A посещено {count} раз')


async def main():
    tasks = [move(f'{name}({i})') for i, name in enumerate(robot_names)]
    await asyncio.gather(*tasks)


asyncio.run(main())
