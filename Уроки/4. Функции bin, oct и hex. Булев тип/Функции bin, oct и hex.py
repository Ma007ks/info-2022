# 10 (int) → 2 (bin), 8 (oct), 10 (str), 16 (hex) — (str)
# n (str) → 10 (int)

# bin(x) — переводит число x (тип int) в двоичную систему счисления (тип str)
# oct(x) — ... в восьмеричную
# hex(x) — ... в шестнадцатеричную

# print(bin(156))
# print(oct(156))
# print(hex(156))

# x = 156
# b = bin(156)

# print(b)
# print(b[2:])
# print(b.replace("0b", ""))
# print(b.removeprefix("0b"))

# print(bin(156)[2:])
# print(bin(15623404230423042403204230).removeprefix("0b"))

# print(bin(10312030210301203012))

# x = 4329425
# print(len(str(x)))
# print(type(x % 10))
# print(type(str(x)[-1]))

s = "1010101010"  # двоичная запись какого-то числа

# Что это за число в десятичной системе счисления?

print(int(s))
print(int(s, base=2))
print(int(s, 3))
print(int(s, 4))
