import logging
import sys

# Настройка базового логгера (не изменять)
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(levelname)s - %(message)s - %(order_id)s - %(amount)s')

logging.info(
    'Новый заказ создан',
    extra={'order_id': input(), 'amount': input()},
)