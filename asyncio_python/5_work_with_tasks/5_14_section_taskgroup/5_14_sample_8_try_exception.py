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
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(get_data(1))
            task2 = tg.create_task(get_data(2))
            task3 = tg.create_task(get_data(0))
            task4 = tg.create_task(file_reader("fake.png"))
            task5 = tg.create_task(file_reader("new_fake.png"))
            task6 = tg.create_task(get_data(0))
        # Результат мы все равно не увидим, так как спровоцируем вызов исключений.
        result = [
            task1.result(),
            task2.result(),
            task3.result(),
            task4.result(),
            task5.result(),
            task6.result(),
        ]
        print("Готово!!!", result)
    # Добавляем обработчики, которые будут группировать ошибки одного типа.
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
    except* Exception as e:
        for error in e.exceptions:
            print(error)


asyncio.run(main())

"""
Давайте сначала рассмотрим устройство обработчика на примере FileNotFoundError, другой устроен 
аналогично:
except* - используется для перехвата и обработки множественных исключений, возникающих в 
асинхронных задачах, группируемых в ExceptionGroup. Используя except* FileNotFoundError as e, 
мы перехватываем все исключения типа FileNotFoundError, которые были сгруппированы в  
ExceptionGroup.

Объект e, представляющий собой ExceptionGroup, содержит атрибут exceptions - кортеж всех  
исключений, сгруппированных в этот ExceptionGroup.

Таким образом, e.exceptions представляет собой кортеж со всеми исключениями FileNotFoundError,  
возникшими в контексте асинхронной группы задач (asyncio.TaskGroup()). Итерируя по e.exceptions,
мы можем обрабатывать каждое исключение индивидуально. Это особенно полезно, когда в асинхронной
операции возникает несколько исключений одного типа и вы хотите обработать каждое из них отдельно.
"""