from unittest.mock import Mock

os = Mock()

print(os.mkdir(r"F:\folder"))
print(os.remove(r"F:\folder"))
print(os.listdir(r"F:\folder"))
