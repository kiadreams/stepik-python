import aiofiles
import asyncio


# Асинхронная функция для чтения файлов
async def read_file_line_by_line(file_path):
    async with aiofiles.open(file_path, mode="r") as file:  # асинхронное открытие файла
        async for line in file:  # итерация по строкам файла
            print(line.strip())


async def main():
    file_path = "example.txt"
    await read_file_line_by_line(file_path)


asyncio.run(main())
