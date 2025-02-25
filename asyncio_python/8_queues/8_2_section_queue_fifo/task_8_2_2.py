import asyncio


patient_info = [
    {
        "name": "Алексей Иванов",
        "direction": "Терапевт",
        "procedure": "Прием для общего осмотра",
    },
    {"name": "Мария Петрова", "direction": "Хирург", "procedure": "Малая операция"},
    {"name": "Ирина Сидорова", "direction": "ЛОР", "procedure": "Осмотр уха"},
    {"name": "Владимир Кузнецов", "direction": "Терапевт", "procedure": "Консультация"},
    {
        "name": "Елена Васильева",
        "direction": "Хирург",
        "procedure": "Хирургическая процедура",
    },
    {"name": "Дмитрий Николаев", "direction": "ЛОР", "procedure": "Промывание носа"},
    {
        "name": "Светлана Михайлова",
        "direction": "Терапевт",
        "procedure": "Рутинный осмотр",
    },
    {
        "name": "Никита Алексеев",
        "direction": "Хирург",
        "procedure": "Операция на колене",
    },
    {"name": "Ольга Сергеева", "direction": "ЛОР", "procedure": "Лечение ангины"},
    {"name": "Анна Жукова", "direction": "Терапевт", "procedure": "Вакцинация"},
]


async def producer(queues, p_info):
    for patient in p_info:
        name, direction, procedure = patient.values()
        match direction:
            case "Терапевт":
                await queues[0].put({"name": name, "procedure": procedure})
            case "Хирург":
                await queues[1].put({"name": name, "procedure": procedure})
            case "ЛОР":
                await queues[2].put({"name": name, "procedure": procedure})
        print(
            f"Регистратор добавил в очередь: {name}, "
            f"направление: {direction}, процедура: {procedure}"
        )
        await asyncio.sleep(0)
    [await queue.put(None) for queue in queues]


async def consumer(queue, doctor_type):
    while True:
        info = await queue.get()
        if info is None:
            break
        name, procedure = info.values()
        print(f"{doctor_type} принял пациента: {name}, процедура: {procedure}")
        await asyncio.sleep(0)


async def main():
    # Полный список вшит в задачу, вставлять его в поле ответа нет необходимости
    # patient_info = []
    therapist = asyncio.Queue()
    surgeon = asyncio.Queue()
    ent = asyncio.Queue()
    tasks = [
        producer((therapist, surgeon, ent), patient_info),
        consumer(therapist, "Терапевт"),
        consumer(surgeon, "Хирург"),
        consumer(ent, "ЛОР"),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
