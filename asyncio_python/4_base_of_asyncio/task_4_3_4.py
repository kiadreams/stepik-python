import asyncio
import random

# Не менять.
random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = [
            "Привет!",
            "Встреча в 15:00",
            "Важное уведомление",
            "Реклама",
        ]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


# Тут пишите ваш код
async def check_mail(server):
    server_is_running = True
    while server_is_running:
        response = await server.check_for_new_mail()
        match response:
            case str() as message:
                print(message)
                server_is_running = False
            case bool():
                print(
                    await server.fetch_new_mail()
                    if response
                    else 'Новых писем нет.'
                )
        await asyncio.sleep(1)


async def main():
    await check_mail(MailServer())


asyncio.run(main())
