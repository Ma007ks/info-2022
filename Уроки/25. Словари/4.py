import json

users = [
    {
        "name": "Илья",
        "surname": "Иванов",
        "age": 15,
        "results": {"math": 10, "rus": 10, "info": 1},
    },
    {
        "name": "Денис",
        "surname": "Вавилов",
        "age": 50,
        "results": {"math": 100, "rus": 100, "info": 70},
    },
    {
        "name": "Сергей",
        "surname": "Рогачев",
        "age": 45,
        "results": {"math": 100, "rus": 100, "info": 100},
    },
    {
        "name": "Костя",
        "surname": "Делягин",
        "age": 10,
        "results": {"math": 1, "rus": 1, "info": 1},
    },
    {
        "name": "Марк",
        "surname": "Кретов",
        "age": 3,
        "results": {"math": 50, "rus": 50, "info": 50},
    },
]

with open("data.json", "w", encoding="utf8") as file:
    json.dump(users, file, ensure_ascii=False, indent=4)
