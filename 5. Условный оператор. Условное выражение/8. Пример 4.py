month = 1  # 1...12

# 1, 2, 12

# if 1 <= month <= 2 or month == 12:
#     print("Зима")
#
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
#
# if month in (1, 2, 12):
#     print("Зима")

if 3 <= month <= 5:
    print("Весна")
elif 6 <= month <= 8:
    print("Лето")
elif 9 <= month <= 11:
    print("Осень")
else:
    print("Зима")
