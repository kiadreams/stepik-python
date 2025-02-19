import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

database = [
    {"название": "Разработать API", "статус": "Завершена"},
    {"название": "Написать документацию", "статус": "Ожидает"},
    {"название": "Провести код-ревью", "статус": "Ожидает"},
]

input_text = "Настроить CI/CD, В процессе"  # В примере будет поступать через ввод

class AsyncListManager:
    @staticmethod
    async def connect() -> None:
        print("Начало работы с базой данных")
        await asyncio.sleep(0.5)

    @staticmethod
    async def disconnect() -> None:
        print("Завершение работы с базой данных")
        await asyncio.sleep(0.5)

    @staticmethod
    async def stage_append(value: dict[str, str]) -> None:
        await asyncio.sleep(1)
        database.append(value)
        print("Новые данные добавлены")


@asynccontextmanager
async def async_session() -> AsyncIterator[AsyncListManager]:
    session = AsyncListManager()
    await session.connect()
    try:
        yield session
    finally:
        await session.disconnect()


async def main() -> None:
    # name, status = input().split(",")
    name, status = input_text.split(",")
    value = {"название": name, "статус": status.strip()}
    async with async_session() as session:
        await session.stage_append(value)
        for item in database:
            print(item)


asyncio.run(main())
