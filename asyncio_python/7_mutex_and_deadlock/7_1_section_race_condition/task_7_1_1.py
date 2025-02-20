import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,
    "Война и мир": 2,
    "Преступление и наказание": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}


async def reserve_book(book):
    if library_catalog[book] > 0:
        await asyncio.sleep(1)
        library_catalog[book] -= 1
        print("Книга успешно зарезервирована.")
    else:
        print("Книга отсутствует. Резервирование отменено.")


async def main():
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(reserve_book(book)) for book in reservation_tasks.values()]
    for book, nums in library_catalog.items():
        print(f'{book}: {nums}')


asyncio.run(main())
