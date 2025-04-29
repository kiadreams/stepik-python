import asyncio
import random

# Создаем события для каждого источника данных
source_a_event = asyncio.Event()
source_b_event = asyncio.Event()
source_c_event = asyncio.Event()


async def fetch_data(source_name, event):
    print(f"{source_name}: Скачивание данных...")
    await asyncio.sleep(random.randint(1, 3))
    print(f"{source_name}: Данные получены.")
    event.set()  # Сигнализируем, что данные готовы


async def analyze_data():
    # ожидаем получения нужных данных
    # await source_a_event.wait()
    # await source_b_event.wait()
    # await source_c_event.wait()
    await asyncio.gather(
        source_a_event.wait(),
        source_b_event.wait(),
        source_c_event.wait(),
    )
    print("Все данные получены. Начало анализа...")
    await asyncio.sleep(2)  # тут может быть анализ данных/отправка их в БД/...
    print("Анализ завершен.")


async def main():
    # Запускаем задачи для получения данных от различных источников
    asyncio.create_task(fetch_data("Источник A", source_a_event))
    asyncio.create_task(fetch_data("Источник B", source_b_event))
    asyncio.create_task(fetch_data("Источник C", source_c_event))

    await analyze_data()


asyncio.run(main())
