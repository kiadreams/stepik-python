import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9,
}
SPEED = 8  # мегабайт в секунду


async def download_file(*args):
    name, size, speed = args
    delay = size / speed
    print(
        f"Начинается загрузка файла: {name}, его размер {size} мб, "
        f"время загрузки составит {delay} сек",
    )
    await asyncio.sleep(delay)
    print(f"Загрузка завершена: {name}")


async def monitor_tasks(tasks):
    done = []
    while tasks:
        # Если в списке есть элементы - печатаю их
        if done:
            print(*done, sep="\n")
        # Итерируюсь по копии списка
        for task in tasks[:]:
            res = (
                f'Задача {task.get_name()}: '
                f'{["в процессе", "завершена"][status := task.done()]}, '
                f"Статус задачи {status}"
            )
            # Если задача готова - убираю ее из списка задач и помещаю
            # результат в список done.
            # Так ухожу от избыточных проверок.
            if status:
                done.append(res)
                tasks.remove(task)
            print(res)
        await asyncio.sleep(1)


async def main():
    tasks = [
        asyncio.create_task(download_file(name, size, SPEED), name=name)
        for name, size in files.items()
    ]
    monitor_task = asyncio.create_task(monitor_tasks(tasks))
    result = await asyncio.gather(*tasks, monitor_task)
    print("Все файлы успешно загружены")


asyncio.run(main())
