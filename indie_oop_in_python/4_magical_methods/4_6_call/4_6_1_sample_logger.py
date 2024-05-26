# Среди ситуаций, где вам будет полезно использовать класс с реализованным
# методом __call__, можно выделить следующие:
#
# -замены функции, которой необходимо хранить состояние своих вызовов
# -предоставление функционала вашего класса через экземпляр
# -замены функции-декоратора классом-декоратором.

# log.py

from datetime import datetime


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __call__(self, message):
        now = datetime.now()
        print(f"{now}: {message}")
        with open(self.log_file, "a") as f:
            f.write(f"{now}: {message}\n")


if __name__ == "__main__":

    logger = Logger("my_log_file.txt")

    if callable(logger):
        print("Объект вызываемый...")

        def get_information():
            logger(f"Start work in {get_information.__name__}:")
            # do some work
            logger("Finished work in get_information")

        def delete_files():
            logger(f"Start work in {delete_files.__name__}")
            # do some work
            logger(f"Finished work in {delete_files.__name__}")

        get_information()
        delete_files()
        get_information()
