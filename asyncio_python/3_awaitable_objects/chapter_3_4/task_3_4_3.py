import asyncio


async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    result = await asyncio.sleep(1, result=x + 1)
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    result = await asyncio.sleep(1, result=x * 2)
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    result = await asyncio.sleep(1, result=x + 3)
    print(f"Третья функция завершилась с результатом {result}")
    return result


async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    result = await asyncio.sleep(1, result=x**2)
    print(f"Четвертая функция завершилась с результатом {result}")
    return result


async def main():
    print("Начало цепочки асинхронных вызовов")
    first_result = await asyncio.create_task(first_function(1))
    second_result = await asyncio.create_task(second_function(first_result))
    third_result = await asyncio.create_task(third_function(second_result))
    final_result = await asyncio.create_task(fourth_function(third_result))
    print(f"Конечный результат цепочки вызовов: {final_result}")


asyncio.run(main())