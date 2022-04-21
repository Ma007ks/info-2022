# 0, 1, 2, ..., 99

# range позволяет сгенерировать любую конечную целочисленную арифметическую прогрессию.

# range(n) — ровно n чисел, начиная с 0 и до n - 1: 0, 1, 2, 3, ..., n - 1
# range(start, finish)
# range(start, finish, step)

print(list(range(5)))
print(list(range(20)))
print(list(range(1)))

print(list(range(10, 20)))
print(list(range(35, 47)))

print(list(range(0, 20, 2)))
print(list(range(20, 0, -3)))

# а) [5, 4, 3, 2, 1, 0, -1, -2] → range(5, -3, -1)
# б) [0, 1, 2, 3, 4, 5, 6] → range(7) = range(0, 7) = range(0, 7, 1)
# в) [3, 5, 7, 9, 11, 13] → range(3, 14, 2)
# г) трёхзначные числа — 100, 101, ..., 998, 999 → range(100, 1000)
# д) нечётные двузначные числа — 11, 13, 15, ..., 99 → range(11, 100, 2)
# е) числа от 507 до 639, оканчивающиеся на 4 — 514, 524, 534, ..., 634 → range(514, 635, 10)
# ж) числа, кратные 7, которые больше 50 и меньше 140 — 56, 63, ..., 133 → range(56, 134, 7)

# range(0, n) = range(n)

# x = 544
# print(10 <= x < 100)
# print(x in range(10, 100))

# print(x in range(514, 635, 10))
# print(507 <= x <= 639 and x % 10 == 4)
#
# print(range(100)[::-1])
#
# print([5, 4, 3, 2, 1, 0, -1, -2])
# print(range(5, -3, -1))
# print(range(-2, 6, 1)[::-1])
#
# print(len(range(5, 25, 2)))

# for x in range(5):
#     print(x, x ** 2)
