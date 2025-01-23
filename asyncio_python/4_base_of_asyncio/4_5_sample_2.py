import asyncio


async def run():
    try:
        task = asyncio.ensure_future(123)
    except TypeError as e:
        print(f"Ошибка: {e}")


asyncio.run(run())
