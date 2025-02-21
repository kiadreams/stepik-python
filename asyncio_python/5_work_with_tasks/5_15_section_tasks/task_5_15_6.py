import asyncio
import random

# Подаётся на вход программы при запуске приложения
ip_dct = {"192.168.0.1": [0, 100], "192.168.0.2": [225, 300], "192.168.2.5": [150, 185]}


async def scan_port(address, port) -> int | None:
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f'Port {port} on {address} is open')
        return port
    return None


async def scan_range(address, start_port, end_port):
    """
    Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    coroutines = [scan_port(address, port) for port in range(start_port, end_port + 1)]
    opened_ports = await asyncio.gather(*coroutines)
    return address, list(filter(lambda x: x is not None, opened_ports))


async def main(dct):
    """
    Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    coroutines = [scan_range(ip, *ports) for ip, ports in dct.items()]
    results = await asyncio.gather(*coroutines)
    for address, ports in results:
        if ports:
            print(f'Всего найдено открытых портов {len(ports)} {ports} для ip: {address}')


# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))
