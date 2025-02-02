import logging
import sys

# Настройка базового логгера (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

logging.info(
    "Пользователь {} успешно подписался на рассылку. Дата подписки: {}".format(
        input(), input(),
    ),
)
