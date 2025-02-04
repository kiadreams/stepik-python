import asyncio


async def my_coroutine():
    print("Корутина запустилась")
    await asyncio.sleep(5)
    print("Корутина завершилась")
    return 42


async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(1)
    print("Функция main продолжает работу")

    try:
        await asyncio.wait_for(task, timeout=2)

        # Получение результата выполнения корутины my_coroutine
        result = task.result()

        # Вывод результата выполнения корутины my_coroutine
        print(f"Результат выполнения корутины my_coroutine: {result}")
    except asyncio.TimeoutError:
        print("Задача не была завершена в указанное время.")


asyncio.run(main())

"""
Однако важно учитывать один момент. Прежде чем вызывать task.result(), 
необходимо убедиться, что задача завершилась. В данных примерах это сделано 
с помощью await task, то есть мы явно ожидаем, выполнения корутины, связанной 
с задачей. Можно также использовать проверку готовности задачи task.done() 
или пытаться получить результаты в блоках try/except, иначе вызовется 
исключение InvalidStateError!!! Все исключения:
 1) InvalidStateError - задача не закончена;
 2) CancelledError - если задача была отменена;
 3) ИСКЛЮЧЕНИЕ КОРУТИНЫ - если корутина вызвала исключение и не обработала 
                            его, то это исключение будет вызвано повторно.
"""
