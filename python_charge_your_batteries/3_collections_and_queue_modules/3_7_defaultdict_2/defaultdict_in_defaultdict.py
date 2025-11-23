from collections import defaultdict
from pprint import pprint


nested_dict = defaultdict(lambda: defaultdict(list))

# Добавляем элементы во вложенные словари
nested_dict["РФ"]["Ростов"].append(1)
nested_dict["РФ"]["Краснодар"].append(2)
nested_dict["Беларусь"]["Минск"].append(3)
nested_dict['Казахстан']
pprint(nested_dict)
