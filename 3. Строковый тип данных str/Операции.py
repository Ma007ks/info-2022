a = 'foo'
b = 'bar'

print("Переменные:")
print(f"{a = }")
print(f"{b = }")
print()

print("Конкатенация (сложение строк):")
c = a + b + b + a
print(f"{c = }")
print()

# Создать строчку, которая состоит из 300 повторений строки ABC
# ABCABC...ABCABC

print("Повторение строки (умножение на число):")
x = "ABC" * 15
print(f"{x = }")
print(f"{'X' * 10 = }")
print(f"{11 * '—' = }")
print()

print("Вычислить длину строки — len — количество символов в строке:")
print(f"{len(x) = }")
print()

print("Методы строк:")
print("x.count(y) — подсчёт числа вхождений строки y в строку x")
print(f"{x.count('ABC') = }")
print(f"{x.count('A') = }")
print(f"{x.count(' ') = }")
print(f"{x.count('abc') = }")
print(f"{'aaaaaaa'.count('aa') = }")
print()

print("x.replace(a, b) — заменяет ВСЕ НЕПЕРЕСЕКАЮЩИЕСЯ вхождения строки a на строку b.")
print("Функция replace возвращает НОВУЮ строчку. Исходная остаётся нетронутой!")
x = 'Привет, мир! Как же хорошо жить!'
y = x.replace('хорошо', 'замечательно')
print(x)
print(y)

print("xyxyxy".replace("x", "y").replace("y", "x").count("y"))

# Строки в Python неизменяемые. То есть когда вы осуществляете какие-то операции, „изменяющие“ строчку,
# вы на самом деле создаёте новую строчку.

print('bc' in 'abcabcbac')
print('bb' in 'abcabcbac')
