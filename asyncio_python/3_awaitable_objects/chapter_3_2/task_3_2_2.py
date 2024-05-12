import asyncio

# Полный словарь students вшит в задачу, вставлять его не нужно
students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57},
}


async def study_course(
    student: str,
    course: str,
    steps: int,
    speed: int,
) -> None:
    print(f"{student} начал проходить курс {course}.")
    reading_time = round(steps / speed, 2)
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {reading_time} ч.")


async def main() -> None:
    # Создание задач с помощью asyncio.create_task для каждого студента
    task_alex = asyncio.create_task(
        study_course("Алекс", *students["Алекс"].values()),
    )
    task_maria = asyncio.create_task(
        study_course("Мария", *students["Мария"].values()),
    )
    task_ivan = asyncio.create_task(
        study_course("Иван", *students["Иван"].values()),
    )
    # Ожидание завершения каждой задачи индивидуально
    await task_alex
    await task_maria
    await task_ivan


asyncio.run(main())
