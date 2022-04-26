# all(iterable)
# any(iterable)

# iterable: list, str, set, tuple, dict, range, generator

# all (ВСЕ/КАЖДЫЙ) возвращает True, если все элементы из iterable дают True (bool(элемент) == True)
# any (КАКОЙ-ЛИБО/ХОТЯ БЫ ОДИН) возвращает True, если есть хотя бы один элемент в iterable, дающий True

a = [2, 6, 3, 4, 8, -9, 10, 4, 5, -7, 5, -2]
b = [2, 6, 4, 8, 16, 10, 4, 8, 0, 4, 2]

# print(all(x > 0 for x in a))
# print(any(x > 0 for x in a))

# print(all(x >= 0 for x in b))
# print(all(x % 2 == 0 for x in b))
# print(all(x % 2 == 0 for x in a))
print(all(a))
print(all(x for x in a))
print(all(b))
print(all(x for x in b))

print(0 not in a)
print(0 not in b)
