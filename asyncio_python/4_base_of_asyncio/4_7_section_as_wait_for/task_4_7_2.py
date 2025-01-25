import asyncio


# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды


# Словарь заклинаний со временем каста
# Полный словарь заклинаний вшит в задачу
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7,
}

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student, spell, cast_time):
    task = asyncio.create_task(asyncio.sleep(cast_time, '1'))
    try:
        await asyncio.wait_for(asyncio.shield(task), max_cast_time)
    except TimeoutError:
        await task
        print(
            f"Ученик {student} не справился с заклинанием {spell}, "
            f"и учитель применил щит. {student} успешно завершает "
            f"заклинание с помощью shield.",
        )
    else:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")

async def main():
    tasks = [
        cast_spell(student, spell, cast_time)
        for student in students
        for spell, cast_time in spells.items()
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
