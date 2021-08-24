import json

with open('group_people.json', 'r') as file:
    data = json.load(file)

    for group in data:
        id_group = group['id_group']
        print(id_group, group)

