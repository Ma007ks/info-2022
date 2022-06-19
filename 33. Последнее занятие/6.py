# 2, 8, 16
# bin, oct, hex

x = (
        4 ** 36
        + 3 * 4 ** 20
        + 4 ** 15
        + 2 * 4 ** 7
        + 49
)


# print(hex(x))
# print(set(hex(x)[2:]))

# while x != 0:
#     digit = x % 16
#     print(digit)
#     x //= 16

# print(hex(2952))

# def tb(x, b):
#     return tb(x // b, b) + [x % b] if x > 0 else []

# def tb(x):
#     return tb(x // 16) + [x % 16] if x > 0 else []

to16 = lambda x: to16(x // 16) + [x % 16] if x > 0 else []

# print(tb(x))
# print(to16(x))

for x in range(4, 17):
    if int('12', x) * int('13', x) == int('222', x):
        print(x)