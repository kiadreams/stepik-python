import threading
import logging
import traceback
import time

# Настройка логгера
logger = logging.getLogger("ThreadLogger")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("threads.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def thread_function():
    try:
        # Код, который может вызвать исключение
        time.sleep(1)
        result = 1 / 0
    except Exception as e:
        logger.error(
            "An error occurred in %s thread:\n%s",
            threading.current_thread().name,
            traceback.format_exc(),
        )


def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
