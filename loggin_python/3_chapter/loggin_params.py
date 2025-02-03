"""


    %(name)s
    Имя логгера, который сгенерировал сообщение.

    %(levelname)s
    Уровень логирования
    (например, DEBUG, INFO, WARNING, ERROR, CRITICAL).

    %(levelno)s
    Целочисленное значение уровня логирования
    (например, 10 для DEBUG, 20 для INFO и т.д.).

    %(pathname)s
    Полный путь к исходному файлу, из которого было вызвано лог-сообщение.

    %(filename)s
    Имя файла (без пути), из которого было вызвано лог-сообщение.

    %(module)s
    Имя модуля (имя файла без расширения .py),
    из которого было вызвано лог-сообщение.

    %(funcName)s
    Имя функции, из которой было вызвано лог-сообщение.

    %(lineno)d
    Номер строки в исходном коде, где было вызвано лог-сообщение.

    %(asctime)s
    Время создания сообщения в формате YYYY-MM-DD HH:MM:SS,mmm
    (где mmm — миллисекунды).

    %(created)f
    Время создания сообщения в формате числа с плавающей точкой,
    представляющего количество секунд, прошедших с начала эпохи
    (с 1 января 1970 года).

    %(msecs)d
    Миллисекунды времени создания сообщения, которые являются частью asctime.

    %(message)s
    Само лог-сообщение, переданное в логгер.

    %(threadName)s
    Имя потока, в котором было вызвано лог-сообщение.

    %(thread)d
    Идентификатор потока, в котором было вызвано лог-сообщение.

    %(processName)s
    Имя процесса, который сгенерировал лог-сообщение.

    %(process)d
    Идентификатор процесса, который сгенерировал лог-сообщение.
"""
