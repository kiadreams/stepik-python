import asyncio
import random


async def task_func(task_id):
    print(f"Старт задачи {task_id}, из корутины task_func")
    await asyncio.sleep(random.uniform(0, 2))
    print(f"Задача {task_id} выполнена в корутине task_func")


async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(task_func(i))
        tasks.append(task)
    print("Все задачи созданы")

    # Цикл, который выполняется, пока есть активные задачи
    while len(tasks) > 0:

        # Ожидание завершения задач
        done, tasks = await asyncio.wait(
            tasks,
            return_when=asyncio.FIRST_COMPLETED,
        )

        # Цикл для вывода сообщения о завершении каждой задачи
        for task in done:
            print(
                f"Задача выполнена- {task.get_name()} и имеет "
                f"флаг- {task.done()}",
            )


asyncio.run(main())
