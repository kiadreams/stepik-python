import asyncio
import random


# Асинхронная функция, имитирующая выполнение задания учеником
async def do_homework(student_id, task_duration):
    print(
        f"Ученик {student_id} начал делать задание, это займет {task_duration} секунд."
    )
    await asyncio.sleep(
        task_duration
    )  # Имитация времени на выполнение задания
    if random.choice([True, False]):  # Случайный выбор успеха или неудачи
        print(f"Ученик {student_id} успешно завершил задание.")
        return f"Задание ученика {student_id} выполнено."
    else:
        print(
            f"Ученик {student_id} столкнулся с проблемой и не смог выполнить задание."
        )
        raise Exception(f"Неожиданная ошибка!")


async def main():
    tasks = [
        asyncio.create_task(
            do_homework(i, random.randint(1, 5)), name=f"Task_{i}"
        )
        for i in range(1, 6)
    ]
    try:
        # Преподаватель раздает задания и собирает результаты
        results = await asyncio.gather(*tasks)
        print("Все задания проверены. Результаты:")
        for result in results:
            print(result)
    except Exception as e:
        # Обработка неожиданного исключения (если такое произойдет)
        print(f"{e} Необходимо отменить все незавершенные задания!")
        # Преподаватель отменяет все незавершенные задания
        for task in tasks:
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    print(f"Задание {task.get_name()} было отменено.")


asyncio.run(main())
