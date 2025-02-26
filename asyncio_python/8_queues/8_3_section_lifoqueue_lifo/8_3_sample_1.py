import asyncio


async def lifoqueue_example():
    # создание LifoQueue с максимальным количеством элементов 3
    lifo_queue = asyncio.LifoQueue(maxsize=3)

    # добавление элементов в очередь
    await lifo_queue.put("Первый элемент")
    await lifo_queue.put("Второй элемент")
    await lifo_queue.put("Третий элемент")

    # получение последнего элемента из очереди
    last_item = await lifo_queue.get()
    print(last_item)

    # получение второго с конца элемента из очереди
    second_last_item = await lifo_queue.get()
    print(second_last_item)

    # получение первого элемента из очереди
    first_item = await lifo_queue.get()
    print(first_item)


asyncio.run(lifoqueue_example())
