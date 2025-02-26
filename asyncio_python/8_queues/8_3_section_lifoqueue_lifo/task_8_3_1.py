import asyncio
from asyncio import LifoQueue


async def autosave(queue):
    for time in range(1, 21):
        await asyncio.sleep(0.1)
        await queue.put(f"Автосохранение {time}")
        print(f"Автосохранение игры через {time} часов")
        if time == 20:
            break


async def simulate_gameplay(queue):
    while True:
        save = await queue.get()
        time = int(save.split()[1])
        if time % 5 == 0:
            print(f"Загружена последняя версия игры: {save}")
            if time == 20:
                break


async def main():
    queue = LifoQueue()
    await asyncio.gather(autosave(queue), simulate_gameplay(queue))
    print("Игра пройдена!")


asyncio.run(main())
