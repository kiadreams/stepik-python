import logging

logging.basicConfig(level=logging.CRITICAL)


def initialize_system():
    try:
        # Предположим, что здесь критическая ошибка
        raise RuntimeError("Critical system initialization failure")
    except RuntimeError as e:
        logging.critical(
            "Critical error during system initialization: %s",
            e,
            exc_info=True,
        )
        raise


initialize_system()
