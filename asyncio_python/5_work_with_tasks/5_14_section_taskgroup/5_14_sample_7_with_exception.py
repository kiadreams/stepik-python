import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception("Нет данных...")
    return {"data": data}


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(get_data(1))
        task2 = tg.create_task(get_data(2))
        task3 = tg.create_task(file_reader("fake.png"))
        task4 = tg.create_task(get_data(0))
    result = [task1.result(), task2.result(), task3.result(), task4.result()]
    print("Готово!!!", result)


asyncio.run(main())

"""
Вот что показывает этот вывод:
    Группа Исключений (ExceptionGroup):
        - Во время выполнения asyncio.TaskGroup() возникли несколько неперехваченных исключений. 
        Python группирует их в ExceptionGroup, что указывает на наличие множественных ошибок.

    Детали исключений:
        - Первое исключение: (FileNotFoundError):
            Произошло в функции file_reader() при попытке открыть файл fake.png, который не был 
            найден.
        - Второе исключение: (Exception с сообщением 'Нет данных...'):
            Вызвано в функции get_data() при попытке обработать данные, где переданное значение 
            равно 0.

    Трассировка вызова (Call Trace):
        Показывает последовательность вызовов функций, приведших к исключению, начиная с вызова 
        asyncio.run(main()) и заканчивая местом в коде, где возникло исключение.

    Обработка исключений:
        Если бы в коде были соответствующие обработчики исключений (except* для FileNotFoundError 
        и Exception), они могли бы перехватить и обработать эти исключения. Однако, поскольку 
        исключения не были обработаны внутри asyncio.TaskGroup, они группируются и выбрасываются 
        как ExceptionGroup.

Таким образом, вывод показывает, что в вашем асинхронном коде произошло два разных исключения, 
которые не были обработаны на уровне задач (TaskGroup), и Python сообщает об этом, группируя 
исключения в ExceptionGroup.
"""
