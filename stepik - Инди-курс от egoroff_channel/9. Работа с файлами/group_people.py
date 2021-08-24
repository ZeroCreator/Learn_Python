import json

with open('group_people.json', 'w') as f:
    data = json.load(f)

    id = 0
    for element in data:

