import asyncio
import random

# await asyncio.gather() возвращает список из результатов задач в том же
# порядке, в каком они переданы в asyncio.gather().  Вне зависимости от
# времени выполнения переданных в asyncio.gather() задач, результаты будут
# сохранены в том порядке, в котором задачи передавались в функцию.
# Важно помнить, что время выполнения задач не влияет на порядок вывода
# результатов

async def my_coroutine(name):
    delay = random.random()
    await asyncio.sleep(delay)
    return f"Корутина {name}: {round(delay, 2)}"

async def main():
    results = await asyncio.gather(*[my_coroutine(i) for i in range(1, 6)])
    print(results)

asyncio.run(main())

