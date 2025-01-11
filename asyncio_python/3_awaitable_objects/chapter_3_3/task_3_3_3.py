import asyncio


async def compute_square(x: int) -> int:
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(3)  # Имитация длительной операции
    return x * x


async def main() -> None:
    # Создаём и запускаем задачи
    tasks = [asyncio.create_task(compute_square(i)) for i in range(10)]
    # Ожидаем завершения всех задач и собираем результаты

    for task in tasks:
        print(f"Результат: {await task}")


asyncio.run(main())
