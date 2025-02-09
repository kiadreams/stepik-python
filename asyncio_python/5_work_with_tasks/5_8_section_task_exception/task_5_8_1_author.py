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
    # Создаем задачи для каждого файла
    tasks = [download_file(file) for file in files]

    # Запускаем задачи и собираем результаты
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Обрабатываем исключения и выводим их на экран
    for result in results:
        if isinstance(result, FileNotFoundError):
            print(result)


# Запуск основной корутины
asyncio.run(main())
