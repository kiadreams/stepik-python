import asyncio


# Список вшит в задачу, вставлять его в поле ответа не нужно
patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]


async def producer(queue):
    for info in patient_info:
        await queue.put(info)
        print(f"Регистратор добавил в очередь: {info}")
        await asyncio.sleep(0)


async def consumer(queue):
    while not queue.empty():
        print(f"Врач принял пациента: {await queue.get()}")
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())
