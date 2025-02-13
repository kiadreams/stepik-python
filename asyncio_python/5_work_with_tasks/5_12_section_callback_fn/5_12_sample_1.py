def greeting(name):  # Определение функции приветствия
    return f"Привет, {name}!"


def farewell(name):  # Определение функции прощания
    return f"Пока, {name}!"


def process_name(callback, name):
    return callback(name)


name = "Студент"

greeting_result = process_name(greeting, name)
print(greeting_result)

farewell_result = process_name(farewell, name)
print(farewell_result)
