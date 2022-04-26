# Мутабельные: list, set, dict
# # Немутабельные: int, float, str, bool, None, tuple
#
# x = [1, 2, 3, 5]
# y = x.copy()
#
# print(x, y)
# print(id(x), id(y))
#
# x.clear()
# print(y)
#
# print(id(x), id(y))

# y = x.copy()
#
# y.append(10)
#
# print(y)
# print(x)

# print(x)
# print(id(x))
#
# x.append(10)
#
# print(x)
# print(id(x))
#
# x.clear()
#
# print(x)
# print(id(x))
#
# print("\nЧисло (int):\n")
#
# y = 254
# print(y, id(y))
#
# y += 5
# print(y, id(y))

Я = ['конфета вкусная', 'конфета вонючая']
Вы = Я

print(Я, Вы)
print(id(Я), id(Вы))

Я.clear()
print(Я, Вы)

Я = ['конфета вкусная', 'конфета вонючая']
Вы = Я[::]

print(Я, Вы)
print(id(Я), id(Вы))

Я.clear()
print(Я, Вы)
