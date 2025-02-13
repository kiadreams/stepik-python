import asyncio


def callback1(task):
    print("Callback 1: Task completed!")
    print("Result:", task.result())


def callback2(task):
    print("Callback 2: Task completed!")
    print("Result:", task.result())


async def my_coro():
    return 42


async def main():
    task = asyncio.create_task(my_coro())

    # Добавление callback-ов к задаче
    task.add_done_callback(callback1)
    task.add_done_callback(callback2)

    await task


asyncio.run(main())

"""
!!! Все callback-и вызываются сразу после завершения задачи в том порядке, 
в котором они были добавлены. !!!
"""
