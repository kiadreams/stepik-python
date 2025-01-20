import asyncio


async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)  # Стандартное время выполнения coroutine1()
    print("Coroutine 1 done")


async def coroutine2():
    print("Coroutine 2 started")
    # Задаем задержку в 2 секунды, чтобы coroutine2() завершалась после coroutine1()
    await asyncio.sleep(2)
    print("Coroutine 2 done")


async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())

    await task1
    # Если закомментировать ожидание второй задачи, то программа завершится 
    # не дождавшись завершения этой задачи!!!
    await task2


asyncio.run(main())
