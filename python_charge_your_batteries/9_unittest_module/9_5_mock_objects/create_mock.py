from unittest.mock import Mock

mock = Mock()
print(mock)

print(mock.current_time)
print(mock.total)
print(mock.get_average())
print(mock.find_max(1, 4, 5, 3))

print(dir(mock))
