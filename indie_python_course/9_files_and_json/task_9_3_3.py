import json

with open('group_people.json', encoding='utf-8') as f:
    data = json.load(f)
groups = {
    sum(p['gender'] == 'Female' and int(p['year']) > 1977
        for p in group['people']): group['id_group'] for group in data
}
print(groups[max(groups)], max(groups))