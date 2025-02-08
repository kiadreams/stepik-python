import asyncio
import aiohttp


"""
Данный код устанавливает такое же имя задачи, как и скачанный файл, это может 
облегчить отладку кода либо сделать код более информативным.
"""


async def download_file(url):
    async with aiohttp.ClientSession() as session:  # Создание асинхронного HTTP-соединения
        async with session.get(
            url
        ) as response:  # Отправка асинхронного GET-запроса
            filename = response.headers.get(
                "content-disposition"
            )  # Извлечение имени файла из заголовков
            if filename:
                filename = filename.split("filename=")[1]
            task = asyncio.current_task()
            task.set_name(
                f"Downloading {filename}"
            )  # Установка имени текущей задачи
            with open(
                filename, "wb"
            ) as f:  # Открытие файла для записи бинарных данных
                while True:
                    chunk = await response.content.read(
                        1024
                    )  # Чтение и запись в файл содержимого ответа по частям
                    if not chunk:
                        break
                    f.write(chunk)
            task.set_name(
                f"Downloaded {filename}"
            )  # Обновление имени текущей задачи после завершения скачивания


async def main():
    urls = [
        "<https://www.example.com/file1.txt>",
        "<https://www.example.com/file2.txt>",
        "<https://www.example.com/file3.txt>",
    ]

    tasks = [asyncio.create_task(download_file(url)) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())
