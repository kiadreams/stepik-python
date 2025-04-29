import asyncio


ip = [
    "192.168.0.3",
    "192.168.0.1",
    "192.168.0.2",
    "192.168.0.4",
    "192.168.0.5"
]

alarm = asyncio.Event()


async def motion_detected():
    await asyncio.sleep(5)
    print('Датчики зафиксировали движение')
    alarm.set()


async def coro_of_sensor(sensor_id):
    print(
        f'Датчик {sensor_id} IP-адрес {ip[sensor_id]}'
        ' настроен и ожидает срабатывания'
    )
    await alarm.wait()
    print(
        f'Датчик {sensor_id} IP-адрес {ip[sensor_id]} активирован, '
        '"Wee-wee-wee-wee"'
    )


async def main():
    tasks = [
        asyncio.create_task(coro_of_sensor(sensor_id))
        for sensor_id in range(5)
    ]
    await asyncio.gather(*tasks, motion_detected())

asyncio.run(main())
