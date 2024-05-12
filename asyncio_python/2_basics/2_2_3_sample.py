import asyncio


async def fetch_data():
    print("Загрузка данных...")
    await asyncio.sleep(2)
    return "Данные"


async def process_data():
    print("Обработка данных...")
    await asyncio.sleep(1)
    return "Данные обработаны"


async def main():
    # fetched_data = asyncio.create_task(fetch_data())
    # processed_data = asyncio.create_task(process_data())
    # await fetched_data
    # await processed_data
    # print(await fetched_data, await processed_data)
    
    fetched_data = await asyncio.create_task(fetch_data())
    processed_data = await asyncio.create_task(process_data())
    print(fetched_data, processed_data)

asyncio.run(main())
