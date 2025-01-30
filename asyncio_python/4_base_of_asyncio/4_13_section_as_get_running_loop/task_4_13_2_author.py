import asyncio


async def send_message(message):
    print(f"Отправка сообщения: {message}")
    print(
        await asyncio.sleep(1, f"Сообщение отправлено: {message}")
    )  # Имитация задержки отправки сообщения


async def receive_message():
    message = "И тебе привет!"
    print(
        await asyncio.sleep(2, f"Сообщение получено: {message}")
    )  # Имитация задержки получения сообщения
    return message


async def main():
    send_task = asyncio.create_task(send_message("Привет"))
    receive_task = asyncio.create_task(receive_message())
    await asyncio.wait([send_task, receive_task])


asyncio.run(main())
