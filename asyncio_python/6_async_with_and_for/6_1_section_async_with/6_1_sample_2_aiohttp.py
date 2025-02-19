import aiohttp
import asyncio

"""
Асинхронные сетевые соединения: при работе с асинхронными сетевыми соединениями, такими как 
HTTP-запросы или взаимодействие с базами данных, async with позволяет автоматически управлять 
соединениями и обеспечивать их закрытие после завершения операций.
"""


async def fetch_url(url):
    # Используем async with для создания асинхронной сессии aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(content)


asyncio.run(fetch_url("https://example.com"))
