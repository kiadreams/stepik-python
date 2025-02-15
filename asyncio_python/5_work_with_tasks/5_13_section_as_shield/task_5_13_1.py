# Время доставки до разных городов:
import asyncio
from asyncio import ALL_COMPLETED

delivery_times = {
    "Москва": 1,
    "Санкт-Петербург": 3,
    "Новосибирск": 7,
    "Екатеринбург": 5,
    "Нижний Новгород": 4,
    "Челябинск": 6,
    "Омск": 7,
    "Красноярск": 8,
    "Владивосток": 9,
    "Хабаровск": 9,
}

# Заказы:
# orders = [(подарок, город, пометка), ...]
orders = [
    ("подарок-1", "Омск", "важно"),
    ("подарок-2", "Хабаровск", "не важно"),
    ("подарок-3", "Москва", "не важно"),
    ("подарок-3", "Санкт-Петербург", "важно"),
]

# Время до нового года:
# days_left =
days_left = 5


# Тут пишите ваш код:
async def deliver(order):
    item, city, _ = order
    await asyncio.sleep(delivery_times.get(city))
    print(f"Подарок {item} успешно доставлен в г. {city}")


async def main():
    tasks = []
    for order in orders:
        tag = order[-1]
        task = asyncio.create_task(deliver(order))
        tasks.append(asyncio.shield(task) if tag == "важно" else task)
    done, pending = await asyncio.wait(tasks, timeout=days_left)
    [task.cancel() for task in pending]
    await asyncio.sleep(max(delivery_times.values()) - days_left)


asyncio.run(main())
