import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    activate_task = await asyncio.create_task(activate_portal(2))
    other_tasks = [
        asyncio.create_task(perform_teleportation(3)),
        asyncio.create_task(recharge_portal(4)),
        asyncio.create_task(check_portal_stability(5)),
        asyncio.create_task(restore_portal(6)),
    ]
    res_tasks = await asyncio.gather(*other_tasks)
    close_task = await close_portal(7)
    print(f'Результат активации портала: {activate_task} единиц энергии')
    print(f'Результат телепортации: {res_tasks[0]} единиц времени')
    print(f'Результат подзарядки портала: {res_tasks[1]} единиц энергии')
    print(f'Результат проверки стабильности: {res_tasks[2]} единиц времени')
    print(f'Результат восстановления портала: {res_tasks[3]} единиц энергии')
    print(f'Результат закрытия портала: {close_task} единиц времени')


asyncio.run(portal_operator())
