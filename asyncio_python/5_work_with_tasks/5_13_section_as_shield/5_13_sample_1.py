import asyncio


# Корутина для задачи, имитирующей выполнение критической задачи.
async def my_coroutine():
    print("Агент приступил к выполнению своего задания.")
    await asyncio.sleep(1)
    # Если задача не была отменена выведем это сообщение
    print("Злодей побежден! Миссия успешно завершена!")


# Корутина для попытки отмены выполнения защищенной задачи.
async def cancel_coroutine(future):
    await asyncio.sleep(0.5)
    future.cancel()
    print("Банг!!! Злодей стреляет в агента!")
    # Можно посмотреть состояние shield_obj после отмены.
    print(f"shield_obj отменен: {future.cancelled()}")
    print(f"shield_obj завершен: {future.done()}")


async def main():
    # Создаем защитный объект shield_obj.
    shield_obj = asyncio.shield(my_coroutine())
    # Тоже, но без барьера
    # shield_obj = asyncio.create_task(my_coroutine())

    # Можно посмотреть тип shield_obj
    # print(f'Тип защитного объекта shield: {type(shield_obj).__name__}') # Future
    print("Бронежилет надет на агента.")
    cancel_task = asyncio.create_task(cancel_coroutine(shield_obj))
    print("Пистолет злодея заряжен.")
    # В случае получения shield_obj asyncio.CancelledError выводим сообщение.
    try:
        await asyncio.gather(shield_obj, cancel_task)
    except asyncio.CancelledError:
        print("Внимание! Бронежилет разрушен!")
    await asyncio.sleep(1)


asyncio.run(main())

"""
Однако следует учитывать, что использование  asyncio.shield() может привести 
к некоторым нежелательным последствиям, если использовать его неосторожно:
    1) Утечка ресурсов: защищённые awaitable объекты могут продолжать 
    использовать ресурсы, даже если остальная программа завершилась.
    2) Зависание программы: программа может не завершиться корректно, если 
    остались незавершённые защищённые awaitable объекты.
    3) Сложность отладки: защита awaitable объектов может затруднить отладку, 
    делая неочевидными причины появления ошибок в работе программы.
    4) Невозможность отмены: защищённые awaitable объекты нельзя просто 
    отменить, что может быть проблематично в некоторых случаях.
Поэтому перед использованием asyncio.shield() необходимо тщательно оценить 
риски и пользу от его использования в конкретной ситуации
"""
