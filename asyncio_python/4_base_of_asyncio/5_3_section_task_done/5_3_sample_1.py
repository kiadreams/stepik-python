import asyncio


async def task_func():
    print("Задача запустилась")
    await asyncio.sleep(1)
    print("Задача завершилась")
    return "Результат выполнения задачи"


async def main():
    task = asyncio.create_task(task_func())
    print('Первая проверка задачи -', task.done())       # Вывод статуса задачи до ее выполнения
    print("Задача создана и помещена в стек вызовов")
    await task
    print('Вторая проверка задачи -', task.done())       # Вывод статуса задачи после ее выполнения
    print("Проверка результата задачи", task.result())


asyncio.run(main())
