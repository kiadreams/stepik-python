import asyncio


news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "Новые исследования о влиянии COVID-19 на здоровье",
    "Конференция разработчиков игр пройдет онлайн",
    "Выставка игр E3 переходит в онлайн-формат"
]


async def analyze_news(keyword, news_l, delay):
    await asyncio.sleep(delay)
    for news in news_l:
        if keyword in news:
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(0)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news("COVID-19", news_list, 7))
    task2 = asyncio.create_task(analyze_news("игр", news_list, 7))
    task3 = asyncio.create_task(analyze_news("новый вид", news_list, 7))

    # Ожидаем выполнения всех задач
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())