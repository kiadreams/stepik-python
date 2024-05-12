import asyncio


async def slow_operation() -> str:
    return "Slow operation result"


async def main() -> None:
    one_coroutine = slow_operation()
    print(one_coroutine)


asyncio.run(main())
