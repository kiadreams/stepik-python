import logging
from logging.handlers import SMTPHandler

# Создание и настройка логгера
logger = logging.getLogger("EmailLogger")
logger.setLevel(
    logging.DEBUG
)  # Уровень логирования: DEBUG для захвата всех сообщений

# Конфигурация SMTPHandler
mail_handler = SMTPHandler(
    mailhost=("smtp.example.com", 587),  # SMTP сервер и порт
    fromaddr="your_email@example.com",  # Адрес отправителя
    toaddrs=["recipient@example.com"],  # Список адресов получателей
    subject="Логи из Python",  # Тема письма
    credentials=(
        "your_email@example.com",
        "your_password",
    ),  # Учетные данные для SMTP
    secure=(),  # Если требуется TLS, используйте ()
)

# Настройка формата сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
mail_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(mail_handler)

# Примеры записей в лог
logger.debug("Это сообщение отладки")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждающее сообщение")
logger.error("Это сообщение об ошибке")
logger.critical("Это критическое сообщение")

"""
    mailhost указывает на SMTP-сервер и порт (например, smtp.example.com 
    и порт 587 для использования TLS).
    fromaddr — адрес отправителя.
    toaddrs — список получателей.
    subject — тема письма.
    credentials — учетные данные для аутентификации (провайдер электронной 
    почты может требовать логин и пароль).
    secure — включает поддержку TLS, если необходимо, в данном случае пустой 
    кортеж (()) указывает на отсутствие специальных требований.
"""