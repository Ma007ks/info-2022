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


# max_info_result = max(user["results"]["info"] for user in users)
# print(max_info_result)


def get_info_result(user):
    return user["results"]["info"]


user_names = {user["name"] for user in users}
print(user_names, type(user_names))

users_ages_map = {f"{user['name']} {user['surname']}": user["age"] for user in users}

print(users_ages_map)
print(users_ages_map["Костя Делягин"])

# user_with_max_info_result = max(users, key=lambda user: user["results"]["info"])
# users_by_info_result = sorted(users, key=get_info_result)
# math_results = [user["results"]["math"] for user in users]
# print(user_with_max_info_result)
# print(users_by_info_result)
# print(math_results)

# for user in users:
#     print(user["name"], user["surname"], user["results"]["math"])
