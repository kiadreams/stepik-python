import asyncio

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
}


# Тут пишите ваш код:
async def deliver(order):
    item, city, flag = order
    delivery_time = delivery_times.get(city)
    if flag == "важно" and delivery_time > main.big_data:
        main.big_data = delivery_time
    print(
        await asyncio.sleep(
            delivery_time, f"Подарок {item} успешно доставлен в г. {city}",
        )
    )


async def main():
    main.big_data = 0
    tasks = [
        (
            asyncio.create_task(deliver(order))
            if order[-1] != "важно"
            else asyncio.shield(deliver(order))
        )
        for order in orders
    ]
    await asyncio.sleep(days_left)
    [task.cancel() for task in tasks if not task.done()]
    await asyncio.sleep(main.big_data - days_left)


asyncio.run(main())
