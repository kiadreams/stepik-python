import logging

logging.basicConfig(level=logging.ERROR)


def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        logging.error("Error: File not found: %s", e, exc_info=True)
        raise


process_file("missing_file.txt")
