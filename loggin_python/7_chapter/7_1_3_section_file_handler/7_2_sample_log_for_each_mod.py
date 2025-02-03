# module_a.py
import logging

logger = logging.getLogger("module_a")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("module_a.log")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("Информация из модуля A")

# module_b.py
import logging

logger = logging.getLogger("module_b")
logger.setLevel(logging.DEBUG)

# Использует свой обработчик со своим файлом вывода
# handler = logging.FileHandler("module_b.log")

# Использует свой обработчик общим файлом вывода
# handler = logging.FileHandler("module_a.log")

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

# Можно подключить один обработчик на два логера
logger.addHandler(handler)
logger.info("Информация из модуля B")
