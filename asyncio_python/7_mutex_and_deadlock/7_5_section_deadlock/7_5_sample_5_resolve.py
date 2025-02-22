import asyncio


async def coroutine_a(b_event, c_event):
    print("Корутина A ожидает B")
    try:
        await asyncio.wait_for(b_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print("Корутина A прекратила ожидание B из-за таймаута")
    c_event.set()  # Сообщаем C, что A завершила ожидание
    print("Корутина A завершила выполнение")


async def coroutine_b(a_event, c_event):
    print("Корутина B ожидает C")
    try:
        await asyncio.wait_for(c_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print("Корутина B прекратила ожидание C из-за таймаута")
    a_event.set()  # Сообщаем A, что B завершила ожидание
    print("Корутина B завершила выполнение")


async def coroutine_c(b_event, a_event):
    print("Корутина C ожидает A")
    try:
        await asyncio.wait_for(a_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print("Корутина C прекратила ожидание A из-за таймаута")
    b_event.set()  # Сообщаем B, что C завершила ожидание
    print("Корутина C завершила выполнение")


async def main():
    # Инициализируем события для управления ожиданием корутин
    a_event = asyncio.Event()
    b_event = asyncio.Event()
    c_event = asyncio.Event()

    # Запускаем корутины
    await asyncio.gather(
        coroutine_a(b_event, c_event),
        coroutine_b(a_event, c_event),
        coroutine_c(b_event, a_event),
    )


asyncio.run(main())
