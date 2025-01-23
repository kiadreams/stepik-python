import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    activ_portal_task = await asyncio.ensure_future(activate_portal(2))
    time_of_teleportation = await asyncio.ensure_future(
        perform_teleportation(1 if activ_portal_task > 4 else activ_portal_task)
    )
    print(f'Результат активации портала: {activ_portal_task} единиц энергии')
    print(f'Результат телепортации: {time_of_teleportation} единиц времени')


asyncio.run(portal_operator())
