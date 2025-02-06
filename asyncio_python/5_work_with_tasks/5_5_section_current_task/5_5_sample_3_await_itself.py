import asyncio


async def main():
    print("Основная корутина запущена")
    # Получение текущей задачи
    task = asyncio.current_task()
    # Задача пытается ожидать сама себя
    try:
        await task
    except RuntimeError as e:
        print(f"Ошибка: {e}")


asyncio.run(main())

"""!!!Задача не может ожидать себя саму.!!!"""
