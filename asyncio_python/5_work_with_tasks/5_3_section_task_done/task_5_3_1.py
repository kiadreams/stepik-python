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


async def download_file(name: str, size: int, speed):
    delay = round(size / speed, 3)
    print(
        f"Начинается загрузка файла: {name}, его размер {size} мб, "
        f"время загрузки составит {delay} сек",
    )
    await asyncio.sleep(delay)
    print(f"Загрузка завершена: {name}")


async def monitor_tasks(tasks):
    is_monitor_active = True
    while is_monitor_active:
        is_monitor_active = False
        for task in tasks:
            name, is_done = task.get_name(), task.done()
            stage = "завершена" if is_done else "в процессе"
            print(f"Задача {name}: {stage}, Статус задачи {is_done}")
            is_monitor_active |= not is_done
        await asyncio.sleep(1)


async def main():
    tasks = [
        asyncio.create_task(download_file(name, size, 8), name=name)
        for name, size in files.items()
    ]
    await asyncio.gather(*tasks, monitor_tasks(tasks))
    print("Все файлы успешно загружены")


asyncio.run(main())
