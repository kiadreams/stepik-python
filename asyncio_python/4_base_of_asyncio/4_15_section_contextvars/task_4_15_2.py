import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar("language")


def set_language(language_code):
    current_language.set(language_code)


async def get_greeting():
    greetings = {"en": "Hello!", "ru": "Привет!", "es": "Hola!"}
    return greetings.get(current_language.get())


async def get_error_message():
    error_messages = {
        "en": "An error occurred.",
        "ru": "Произошла ошибка.",
        "es": "Ocurrió un error.",
    }
    return error_messages.get(current_language.get())


async def test_user_actions(language_code):
    set_language(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main():
    tasks = (
        asyncio.create_task(test_user_actions(code))
        for code in ("en", "ru", "es")
    )
    await asyncio.gather(*tasks)


asyncio.run(main())
