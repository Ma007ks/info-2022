# Функция input() считывает пользовательский ввод, причём ровно одну строку (!) и возвращает её.
# Возвращаемый тип данных — str.

# x = int(input())
# y = int(input())
#
# print(x + y)

# 23 14
# 37

# s = input()  # "23 14"
# x, y = s.split()
# x = int(x)
# y = int(y)
#
# print(x + y)

# x, y, z = map(int, input().split())
# x, y, z = int(x), int(y), int(z)

# print(x + y + z)

# 24 14 9 24 9234 2349 2439 24
print(sum(map(int, input().split())))
