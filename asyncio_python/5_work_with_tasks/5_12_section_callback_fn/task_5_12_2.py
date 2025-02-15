import asyncio


codes = [
    "56FF4D",
    "A3D2F7",
    "B1C94A",
    "F56A1D",
    "D4E6F1",
    "A1B2C3",
    "D4E5F6",
    "A7B8C9",
    "D0E1F2",
    "A3B4C5",
    "D6E7F8",
    "A9B0C1",
    "D2E3F4",
    "A5B6C7",
    "D8E9F2",
]

messages = [
    "Привет, мир!",
    "Как дела?",
    "Что нового?",
    "Добрый день!",
    "Пока!",
    "Спокойной ночи!",
    "Удачного дня!",
    "Всего хорошего!",
    "До встречи!",
    "Счастливого пути!",
    "Успехов в работе!",
    "Приятного аппетита!",
    "Хорошего настроения!",
    "Спасибо за помощь!",
    "Всего наилучшего!",
]


async def print_code(code):
    print("Код:", code)


async def show_callback(task):
    code = task.get_name()
    index = codes.index(code)
    num = int(code[-1], base=16)
    print(
        "Сообщение:",
        messages[index] if num % 2 else "Неверный код, сообщение скрыто",
    )
    await print_code(code)


async def async_fn():
    pass


async def main():
    tasks = []
    for i, code in enumerate(codes):
        task = asyncio.create_task(async_fn(), name=code)
        task.add_done_callback(
            lambda t: asyncio.create_task(show_callback(t)),
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())
