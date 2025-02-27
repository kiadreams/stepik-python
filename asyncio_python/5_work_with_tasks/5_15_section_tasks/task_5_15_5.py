import random
import asyncio


async def scan_port(address, port):
    if await asyncio.sleep(1, random.randint(0, 1)):
        print(f'Порт {port} на адресе {address} открыт')
        return port
    return None


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = [
        asyncio.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)
    ]
    opened_ports = list(filter(lambda x: x is not None, await asyncio.gather(*tasks)))
    if opened_ports:
        print(f'Открытые порты на адресе {address}: {opened_ports}')
    else:
        print(f'Открытых портов на адресе {address} не найдено')


asyncio.run(scan_range("192.168.0.1", 80, 85))
