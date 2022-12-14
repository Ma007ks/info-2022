# set — множество

# 1) не хранит порядок элементов → нет индексов и срезов
# 2) не хранит дубликаты → важно лишь наличие или отсутствие объектов

# Для чего нужно?
# 1) легко и быстро удалять повторы объектов из коллекций
# 2) гарантировать различность элементов
# 3) очень быстро работает проверка вхождения элемента (in)

# Как создать множество?

# print("Пустое множество:", set())
# print("Перечислением элементов:", {3, 7, 2, 3, 3, 7, 1, 103})
# print("На основе списка:", set([34, 2, 6, 1]))
# print("На основе range:", set(range(10)))
# print("На основе строки:", set("привет мир как дела"))

# Операции с множествами
# x = {1, 3, 5, 7, 9, 11, 13, 15, 17}
# y = {1, 2, 5, 6, 8, 12, 14, 15, 16. Задание 12, 17}
# z = set(range(5, 13))
#
# print(f"{x = }")
# print(f"{y = }")
# print(f"{z = }")
#
# print(f"Объединение множеств: {x | y = }")
# print(f"Пересечение множеств: {x & y = }")
# print(f"Разность множеств: {x - y = }")
# print(f"Разность множеств: {y - x = }")
# print(f"Симметрическая разность: {x ^ y = }")

# Изменение множества
# x = set()
# x.add(5)  # добавить один элемент в множество
# x.add("bar")
# print(x)
#
# x.update("foo")
# x.update([2, 3, 5])
# print(x)
#
# x.remove(5)
# print(x)

# print({1, 2, 3} == {3, 3, 2, 1})
# print({2, 3} < {2, 3, 5})
# print(5 in {2, 3, 5})
# print(5 in {2, 3, 7})

# print(len({3, 2, 3, 4, 1, 2, 3}))

# Есть список чисел. Вывести True, если в нём нет повторов, то есть все элементы различны, иначе False.
x = [3, 6, 1, 2, 7, 3, 5]  # False
y = [1, 6, 2, 8, 4, 5]  # True
z = []  # True

print(len(set(x)) == len(x))
print(len(set(y)) == len(y))
print(len(set(z)) == len(z))

a = "егэ"
print(len(set(a)) == len(a))

b = "молоко"
print(len(set(b)) == len(b))
