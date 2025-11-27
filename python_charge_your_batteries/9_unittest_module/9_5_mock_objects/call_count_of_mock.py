from unittest.mock import Mock

# Создаем мок-объект
mock = Mock()

# Вызываем его несколько раз
mock()
mock()

mock.get_message()

# Проверяем количество вызовов
print(mock.call_count)
print(mock.get_message.call_count)
