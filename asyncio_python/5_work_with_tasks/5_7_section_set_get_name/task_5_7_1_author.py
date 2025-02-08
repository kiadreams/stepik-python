import asyncio


# Товары на складе:
warehouse_store = {
    "Диван": 15,
    "Обеденный_стол": 10,
    "Офисное_кресло": 25,
    "Кофейный_столик": 12,
    "Кровать": 8,
    "Книжный_шкаф": 20,
    "ТВ-тумба": 7,
    "Шкаф": 9,
    "Письменный_стол": 18,
    "Тумбочка": 14,
    "Комод": 11,
    "Барный_стул": 22,
    "Угловой_диван": 4,
    "Двухъярусная_кровать": 3,
    "Шезлонг": 2,
    "Консольный_столик": 16,
    "Кресло": 17,
    "Туалетный_столик": 19,
    "Книжный_стеллаж": 24,
    "Банкетка": 10,
    "Обеденный_стул": 28,
    "Кресло-качалка": 15,
    "Шкаф-купе": 18,
    "Табуретка": 40,
    "Стеллаж": 13,
    "Кресло-мешок": 5,
    "Кухонный_гарнитур": 6,
    "Журнальный_столик": 8,
    "Витрина": 7,
    "Полка": 30,
}

# Заказ:
order = {"Диван": 5, "Обеденный_стол": 3, "Табуретка": 50, "Гардероб": 1}


async def check_store(item, quantity):
    exist = warehouse_store.get(item, 0)
    status = ["Отсутствует", "Частично в наличии", "В наличии"][
        bool(exist) + (exist >= quantity)
    ]
    asyncio.current_task().set_name(f"{status}: {item}")


async def main():
    tasks = [
        asyncio.create_task(check_store(item, quantity))
        for item, quantity in order.items()
    ]
    result = await asyncio.gather(*tasks)
    print(*sorted(task.get_name() for task in tasks), sep="\n")


asyncio.run(main())
