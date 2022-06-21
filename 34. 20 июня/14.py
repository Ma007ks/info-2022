from sys import setrecursionlimit

setrecursionlimit(10000)

x = (343 ** 515
     - 6 * 49 ** 520
     + 5 * 49 ** 540
     - 3 * 7 ** 530
     - 550)


def tb(x, b):
    return tb(x // b, b) + [x % b] if x > 0 else []


count = 0
print(tb(x, 7).count(6))

while x != 0:
    if x % 7 == 6:
        count += 1
    x //= 7

print(count)
