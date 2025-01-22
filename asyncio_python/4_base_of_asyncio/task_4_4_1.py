import asyncio

places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище",
]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name, delay=0.1):
    for place in places:
        await asyncio.sleep(delay)
        print(f"{name} {place}...")


async def main():
    tasks = [asyncio.create_task(counter(role, 1)) for role in roles]
    # Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    await asyncio.gather(*tasks)


asyncio.run(main())
