import asyncio
import contextvars

user_context = contextvars.ContextVar("user_context")


def log_authentication():
    print(f"User {user_context.get()} authenticated")
    # пытаемся изменить контекстную переменную
    user_context.set("Unknown user")
    print(f"User {user_context.get()} authenticated_2")


async def log_authentication_coro():
    print(f"User {user_context.get()} authenticated")
    # пытаемся изменить контекстную переменную
    user_context.set("Unknown user")
    print(f"User {user_context.get()} authenticated_2")


async def authenticate_user(user_id):
    token = user_context.set(user_id)
    try:
        # ВАРИАНТ 1
        # log_authentication()
        # ВАРИАНТ 2
        await log_authentication_coro()
        # ВАРИАНТ 3
        # await asyncio.create_task(log_authentication_coro())
    finally:
        # Проверка, была ли изменена конекстная переменная
        print(f"User {user_context.get()} logout")
        user_context.reset(token)


async def main():
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie"),
    )


asyncio.run(main())
