import asyncio
import contextvars

# Определяем контекстную переменную
user_context = contextvars.ContextVar("user_context")


async def authenticate_user(user_id):
    # Устанавливаем значение контекстной переменной
    token = user_context.set(user_id)
    try:
        # Эмулируем аутентификацию пользователя
        await asyncio.sleep(1)  # Задержка для имитации асинхронной операции
        print(f"User {user_context.get()} authenticated")
    finally:
        # Удаляем значение после завершения
        user_context.reset(token)


async def main():
    # Запускаем аутентификацию для разных пользователей
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie"),
    )


asyncio.run(main())
