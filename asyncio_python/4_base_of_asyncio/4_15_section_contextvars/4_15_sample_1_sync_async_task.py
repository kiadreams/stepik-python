import asyncio
import contextvars

user_context = contextvars.ContextVar("user_context")


# Синхронная функция для логирования
def log_authentication():
    print(f"User {user_context.get()} authenticated")


# Корутина для логирования
async def log_authentication_coro():
    print(f"User {user_context.get()} authenticated")


async def authenticate_user(user_id):
    token = user_context.set(user_id)
    try:
        # ВАРИАНТ 1: синхронная функция
        log_authentication()
        # ВАРИАНТ 2: корутина
        await log_authentication_coro()
        # ВАРИАНТ 3: задача
        await asyncio.create_task(log_authentication_coro())
    finally:
        user_context.reset(token)


async def main():
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie"),
    )


asyncio.run(main())
