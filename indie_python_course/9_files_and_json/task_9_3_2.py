import json

with open('manager_sales.json', encoding='utf-8') as f:
    data: dict[list[dict]] = json.load(f)
managers = {
    sum(int(car['price']) for car in m['cars']): m['manager'] for m in data
}
manager = managers[max(managers)]
print(manager['first_name'], manager['last_name'], max(managers))

