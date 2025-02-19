import asyncio

# База данных
database = [
    {"название": "Разработать API", "статус": "Завершена"},
    {"название": "Написать документацию", "статус": "Ожидает"},
    {"название": "Провести код-ревью", "статус": "Ожидает"},
]

input_text = "Настроить CI/CD, В процессе"  # В примере будет поступать через ввод


# Не менять
class AsyncListManager:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def connect(self):
        print("Начало работы с базой данных")
        await asyncio.sleep(0.5)

    async def disconnect(self):
        print("Завершение работы с базой данных")
        await asyncio.sleep(0.5)

    async def stage_append(self, value):
        await asyncio.sleep(1)
        database.append(value)
        print("Новые данные добавлены")


# Тут пишите ваш код
async def main():
    async with AsyncListManager() as manager:
        # title, status = input_text.strip().split(", ") # Для проверки
        title, status = input().strip().split(", ")
        await manager.stage_append({"название": title, "статус": status})
        for stage in database:
            print(stage)


asyncio.run(main())
