import asyncio


async def task_func(task_id):
    if task_id == 2:
        raise TypeError('моё исключение')
    print(f"Задача {task_id} выполнена")
    return task_id


async def main():
    # Создаем несколько задач
    tasks = [
        asyncio.create_task(task_func(i), name=f"Task-{i}") for i in range(5)
    ]

    # Ожидаем завершения всех задач
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_EXCEPTION,
    )
    print(len(done))
    # Проверяем, что все задачи завершены
    assert not pending, f"{len(pending)} ожидающих задач"
    for task in tasks:
        print(
            f"Результат задачи {task.get_name()}:",
            task.result() if task.exception() is None else task.exception(),
        )


asyncio.run(main())
