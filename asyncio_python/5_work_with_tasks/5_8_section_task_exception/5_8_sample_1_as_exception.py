import asyncio


"""
Что возвращает task.exception():

    Если обернутая корутина завершилась без исключений, этот метод вернет None.
    Если обернутая корутина вызвала исключение, то это исключение будет возвращено.
    Если задача была отменена, этот метод вызовет исключение CancelledError.
    Если задача еще не завершена, этот метод вызовет исключение InvalidStateError.

"""


async def raise_exception():
    # Генерируем ошибку RuntimeError
    raise RuntimeError("--Установленное исключение--")


async def main():
    task = asyncio.create_task(raise_exception())
    await asyncio.sleep(0.1)
    try:
        await task
    except Exception as e:
        print(f"Пойманное исключение: {e}")
    # Получаем исключение, которое возникло во время выполнения задания (если оно возникло)
    exception = task.exception()
    if exception:
        print(f"Тут можно обработать возникшее исключение: {exception}")


asyncio.run(main())
