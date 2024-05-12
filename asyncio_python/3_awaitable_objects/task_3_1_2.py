import asyncio


async def coro1() -> None:
    print("coro_1 says, hello coro_2!")


async def coro2() -> None:
    print("coro_2 says,hello  coro_1!")


async def main() -> None:
    await asyncio.gather(coro1(), coro2())


asyncio.run(main())
