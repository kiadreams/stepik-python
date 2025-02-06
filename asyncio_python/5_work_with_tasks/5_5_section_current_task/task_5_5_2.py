import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {
        "name": "Мария Петрова",
        "report": "Прогнозирование движения денежных средств",
        "load_time": 4,
    },
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {
        "name": "Елена Кузнецова",
        "report": "Обзор операционных расходов",
        "load_time": 2,
    },
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10},
]


async def download_data(report):
    report_name = report["report"]
    name = report["name"]
    if name == "Дмитрий Орлов":
        print(
            f"Загрузка отчета {report_name} для пользователя {name} остановлена. "
            "Введите новые данные"
        )
        await cancel_task(asyncio.current_task())
    await asyncio.sleep(report["load_time"])
    return f"Отчет: {report_name} для пользователя {name} готов"


async def cancel_task(task):
    task.cancel()


async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        try:
            print(await done.pop())
        except asyncio.CancelledError:
            continue


asyncio.run(main())
