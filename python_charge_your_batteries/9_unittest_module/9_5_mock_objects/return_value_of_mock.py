from unittest.mock import Mock


mock = Mock()
mock.get_message.return_value = {
    'id': 5,
    'message': 'hello world'
}

print(mock.get_message)
print(mock.get_message())
