import asyncio
import random


# Создаем событие
event = asyncio.Event()


# Определяем корутину number_generator, которая генерирует случайные числа
async def number_generator():
    # Генерируем список из 5000 случайных чисел от 1 до 100
    lst = [random.randint(1, 100) for x in range(5000)]
    # Перебираем сгенерированный список
    for en, i in enumerate(lst):
        await asyncio.sleep(random.uniform(0, 0.1))
        if i == 33:
            event.set()
        print(f"Генерируем число: {i}")
        if event.is_set():
            print(f"Событие наступило, число {i} найдено, через {en} попыток")
            break


async def main():
    await asyncio.create_task(number_generator())


asyncio.run(main())
