import asyncio


async def read_queue(queue):
    while True:                       # запускаем бесконечный цикл для чтения элементов из очереди
        await asyncio.sleep(1)
        item = await queue.get()                    # получаем элемент из очереди
        print("Получен элемент из очереди:", item)  # выводим полученный элемент
        # await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()                         # создаем очередь
    asyncio.create_task(read_queue(queue))          # создаем задачу для корутины read_queue
    await queue.put("Первый элемент")               # добавляем первый элемент в очередь
    await queue.put("Второй элемент")               # добавляем второй элемент в очередь
    await asyncio.sleep(2.1)


asyncio.run(main())