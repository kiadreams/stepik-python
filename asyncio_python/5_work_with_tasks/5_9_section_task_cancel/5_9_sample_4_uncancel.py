import asyncio
import random


"""
Если вы попробуете в разных вариантах использовать task.uncancel() в основной корутине, вы 
увидите, что задача все равно отменилась и исключение asyncio.CancelledError было проброшено в 
основной код. При этом, если вызвать task.uncancel() в корутине, которая может быть отменена, в 
блоке except, перехватывающем asyncio.CancelledError, то в таком случае корутину можно запустить 
дальше. 
"""


async def download():
    download_progress = random.random()
    print(f"Успешно загружено {int(download_progress * 100)}%")
    while download_progress < 1:
        try:
            await asyncio.sleep(2)  # имитация загрузки файла
            print("Загрузка завершена")
            break
        except asyncio.CancelledError:
            print("Загрузка отменена")
            if download_progress > 0.5:
                print("Прогресс скачивания более 50%, возобновляем загрузку")
                # отменяем действие cancel()
                asyncio.current_task().uncancel()
            else:
                print("Прогресс скачивания менее 50%, загрузка остановлена")
                raise


async def main():
    task = asyncio.create_task(download())
    await asyncio.sleep(1)
    task.cancel()  # Отменяем задачу
    try:
        await task
    except asyncio.CancelledError:
        print("Загрузка была отменена")


asyncio.run(main())
