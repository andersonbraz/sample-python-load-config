import json

with open('config/settings.json', 'r') as file:
    data = json.load(file)

for item in data:
    print(item["owner"])
