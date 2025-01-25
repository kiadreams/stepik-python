import asyncio


async def long_running_task():
    await asyncio.sleep(10)
    return "Завершение работы защищенной корутины long_running_task() после timeout"


async def main():
    task = asyncio.create_task(long_running_task())
    try:
        # Используем shield для защиты задачи от отмены
        await asyncio.wait_for(asyncio.shield(task), timeout=5)

    except TimeoutError:
        print("Задача не была завершена в установленное время")
        result = await task
        print(result)


asyncio.run(main())
