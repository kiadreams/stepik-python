import asyncio


async def print_event_loop(loop):
    current_loop = asyncio.get_running_loop()
    if current_loop == loop:
        print("Переданный цикл событий активен")
    else:
        print("Переданный цикл событий не активен")
        print(
            f"Переданный цикл:{id(loop)}, - активный?...: {loop.is_running()}"
            f"\nТекущий цикл: {id(asyncio.get_running_loop())} - "
            f"активный?...: {asyncio.get_running_loop().is_running()}",
        )


loop = asyncio.new_event_loop()
asyncio.run(print_event_loop(loop))
