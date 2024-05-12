import asyncio


async def async_func() -> None:

    def sync_func() -> int:
        return 42

    number = sync_func()
    print(number)


asyncio.run(async_func())
