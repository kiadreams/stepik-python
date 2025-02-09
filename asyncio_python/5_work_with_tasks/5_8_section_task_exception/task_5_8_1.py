import asyncio

# files = ['image.png', 'file.csv', 'file1.txt'... ]  полный список вшит в задачу
# missed_files = [...] список пропущенных файлов "спрятан" внутри задачи

files = ["image.png", "file.csv", "file1.txt", "file2.txt", "file6.txt"]
missed_files = ["file.csv", "file2.txt"]


# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f"Файл {file_name} не найден")
    else:
        await asyncio.sleep(1)
        return f"Файл {file_name} успешно скачан"


# Ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(download_file(file)) for file in files]
    await asyncio.gather(*tasks, return_exceptions=True)
    exceptions = [task.exception() for task in tasks if task.exception()]
    print(*exceptions, sep='\n')


asyncio.run(main())
