n = (
    8 ** 547
    + 3 * 8 ** 635
    + 3 * 8 ** 90
    - 4 * 8 ** 551
    - 8 ** 506
    + 3 * 8 ** 183
    - 5 * 8 ** 486
    + 3 * 8 ** 86
    + 227
)


print(oct(n)[2:].count("7"))
print(f"{n:o}".count("7"))
print(format(n, "o").count("7"))

count_7 = 0

while n != 0:
    d = n % 8  # получить младшую цифру
    if d == 7:
        count_7 += 1
    n //= 8  # удалить младшую цифру

print(count_7)


def tb(n, b):
    return tb(n // b, b) + [n % b] if n > 0 else []


print(tb(n, 8).count(7))


def tb(n):
    return tb(n // 8) + [n % 8] if n else []


print(tb(n))
