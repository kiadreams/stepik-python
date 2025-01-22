import asyncio


async def monitor_cpu(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        show_status(task_name, status)


async def monitor_memory(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        show_status(task_name, status)


async def monitor_disk_space(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        show_status(task_name, status)


def show_status(task_name, status: str):
    print(f"[{task_name}] Статус проверки: {status}")
    if status == "Катастрофически":
        print(
            f"[{task_name}] Критическое состояние достигнуто. "
            f"Инициируется остановка...",
        )


async def main():
    status_list = [
        "Отлично",
        "Хорошо",
        "Удовлетворительно",
        "Средне",
        "Пониженное",
        "Ниже среднего",
        "Плохо",
        "Очень плохо",
        "Критично",
        "Катастрофически",
    ]
    tasks = [
        asyncio.create_task(monitor_cpu(status_list), name="CPU"),
        asyncio.create_task(monitor_memory(status_list), name="Память"),
        asyncio.create_task(
            monitor_disk_space(status_list),
            name="Дисковое пространство",
        ),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
