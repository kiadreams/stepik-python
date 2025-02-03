import logging
import traceback

# Настройка логгера
logger = logging.getLogger("StackTraceLogger")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler("app.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def risky_function():
    try:
        # Код, который может вызвать исключение
        result = 1 / 0
    except Exception as e:
        # Логирование трассировки стека
        logger.error("An error occurred:\n%s", traceback.format_exc())


def main():
    risky_function()


if __name__ == "__main__":
    main()

"""
    traceback.format_exc(): Возвращает строковое представление трассировки
    стека текущего исключения.

    traceback.format_exception(exc_type, exc_value, exc_traceback):
    Форматирует исключение, переданное в виде типа, значения и объекта
    трассировки стека, возвращая список строк.

    traceback.format_tb(tb): Форматирует трассировку стека, предоставленную
    в виде объекта tb, возвращая список строк.

    traceback.extract_tb(tb): Извлекает информацию о трассировке стека из
    объекта tb, возвращая список объектов FrameSummary*.

    traceback.extract_stack(f=None, limit=None): Извлекает информацию о
    текущей трассировке стека, возвращая список объектов FrameSummary*.
    Параметр f позволяет указать фрейм, от которого следует начать извлечение,
    а limit ограничивает количество возвращаемых элементов.

    traceback.print_exc(file=None, limit=None, chain=True): Печатает
    трассировку стека текущего исключения на указанный поток (по умолчанию
    на sys.stderr).

    traceback.format_stack(f=None, limit=None): Форматирует текущую
    трассировку стека, возвращая список строк. Параметр f позволяет указать
    фрейм, от которого следует начать форматирование, а limit ограничивает
    количество возвращаемых строк.

* - FrameSummary — это объект, предоставляемый модулем traceback, который
представляет один фрейм (кадр) из трассировки стека. Он содержит информацию о
конкретной точке в программе, где произошла ошибка или где был создан фрейм
стека.

FrameSummary включает следующие атрибуты:

    filename: Имя файла, где произошла ошибка.
    lineno: Номер строки в файле, где произошла ошибка.
    name: Имя функции или метода, где произошла ошибка.
    line: Строка кода, соответствующая ошибке.
"""
