# Сформировать список из 100 нулей

# lst = [0] * 100
# print(lst)
# print(len(lst))

# lst = []
# for i in range(100):
#     lst.append(0)
# print(lst)

# Сформировать список из квадратов первых 100 натуральных чисел:
# [1, 4, 9, 16. Задание 12, 25, 36, ..., 10000]
# squares = []
# for x in range(1, 101):
#     squares.append(x ** 2)
# print(squares)

lst = [-101, 25, 12, -7, -8, 15, 0, 20, 4, -1, 7, -2, -3, 8, 1]

# На основе списка lst сформировать список из его отрицательных элементов:
# negative = [-101, -7, -8, -1, -2, -3]

negatives = []
for x in lst:
    if x < 0:
        negatives.append(x)

print(negatives)

# odd — нечётный, even — чётный
odds = []  # список нечётных элементов
for x in lst:
    if x % 2 == 1:
        odds.append(x)

print(odds)
print(min(odds))
