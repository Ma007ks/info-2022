import json

with open("data.json", encoding="utf8") as file:
    users = json.load(file)

print(users)
