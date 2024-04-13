import asyncio


async def cook_dish(n):
    print(f"Повар {n} начинает готовить")
    await asyncio.sleep(4 - n)
    print(f"Повар {n} закончил готовить")
    return f"Блюдо от повара {n}"

# Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.


async def main():
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)]
    print(*await asyncio.gather(*tasks), sep='; ')


asyncio.run(main())
