import asyncio


async def fethc_data():
    print("Начинаем загрузку данных")
    await asyncio.sleep(2)  # Имитация асинхронной операции ввода-вывода
    print("Данные загружены")
    return {'data': 123}

async def main():
    # Создаем список из 500 асинхронных задач, используя функцию fetch_data
    tasks = [fethc_data() for _ in range(500)]
    # Используем asyncio.gather для одновременного запуска всех задач
    result = await asyncio.gather(*tasks)
    # Для упрощения вывода в консоль покажем количество успешно выполненных задач
    print(f"Загружено {len(result)} задач")

asyncio.run(main())
