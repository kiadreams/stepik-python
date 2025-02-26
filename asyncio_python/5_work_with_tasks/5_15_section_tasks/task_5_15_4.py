# Объявите функцию publish_post: принимает на вход текст поста и имитирует
# публикацию нового поста на блоге Васи


# Объявите функцию notify_subscribers: принимает на вход список подписчиков и
# имитирует отправку уведомления каждому подписчику

import asyncio


async def publish_post(text: str) -> str:
    post = f"Пост опубликован: {text}"
    print(await asyncio.sleep(1, post))
    return post


async def notify_subscribers(subscribers: list[str]) -> None:
    async def notify_subscriber(subscriber):
        print(await asyncio.sleep(1, f"Уведомление отправлено {subscriber}"))
    coroutines = [notify_subscriber(subscriber) for subscriber in subscribers]
    await asyncio.gather(*coroutines)



async def main():
    post_text = "Hello world!"
    subscribers = [
        "Alice",
        "Bob",
        "Charlie",
        "Dave",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        "Isabella",
        "Jack",
    ]
    await asyncio.create_task(publish_post(post_text))
    await asyncio.create_task(notify_subscribers(subscribers))


# запускаем асинхронную функцию main()
asyncio.run(main())