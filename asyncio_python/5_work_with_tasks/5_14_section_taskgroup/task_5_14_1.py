import asyncio

# files = ['image.png', 'file.csv', 'file1.txt'... ]  полный список вшит в задачу
files = ["image.png", "file.csv", "file1.txt"]


async def download_file(file_name):
    await asyncio.sleep(1)
    # функция вшита в задачу, она имитирует скачивание файла с сервера, генерирует несколько типов ошибок:
    raise FileNotFoundError(f"{file_name}: Файл не найден")
    # raise PermissionError(f'{file_name}: Нет прав на доступ к файлу')
    # raise TimeoutError(f'{file_name}: Превышено время ожидания для скачивания файла')


# ваш код пишите тут:
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(download_file(file_name)) for file_name in files]
    except* Exception as e:
        [print(exception) for exception in e.exceptions]


asyncio.run(main())
