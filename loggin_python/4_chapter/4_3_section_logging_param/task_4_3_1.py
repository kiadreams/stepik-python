import logging
import sys

# Настройка базового логгера (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def user_action(user_name, action, timestamp):
    logging.info(
        "Пользователь %s выполнил действие '%s' в %s",
        user_name,
        action,
        timestamp,
    )


# Примеры вызова функции
user_action("Иван", "вошел в систему", "2024-09-03 14:00")
user_action("Мария", "обновила профиль", "2024-09-03 15:30")
