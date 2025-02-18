"""
TaskGroup призван объединить функциональность asyncio.create_task() и asyncio.gather() в одном
инструменте. Это означает, что работа с классом asyncio.TaskGroup сочетает в себе API создания
задач с удобным и надежным способом ожидания завершения всех задач в группе.
Обработка группы корутин позволяет объединить в себе функции:
    - Ожидание завершения всех задач.
    - Отмена всех задач, если хотя бы одна задача завершится с ошибкой.
    - Обработка исключения, возникшего в любой задаче.
Объект класса asyncio.TaskGroup реализует интерфейс асинхронного контекстного менеджера, и это
предпочтительное использование класса. Это означает, что экземпляр класса создается и используется
через выражение async with .
    async with asyncio.TaskGroup() as tg:
"""
import asyncio


async def some_coro(num):
    await asyncio.sleep(num)
    return num / 2


async def main():
    # Создаем группу задач.
    async with asyncio.TaskGroup() as tg:
        # Создаем в группе задачу.
        task = tg.create_task(some_coro(2))
    print(f"Задача выполнена с результатом: {task.result()}.")

asyncio.run(main())
