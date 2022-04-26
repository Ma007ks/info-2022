# Простые числа — числа, имеющие ровно два делителя: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37

# 8 = 2 * 2 * 2 = 2 * 2^2 → 4
# 18 = 2 * 3 * 3 = 2 * 3^2 → 9
# 50 = 2 * 5 * 5 = 2 * 5^2 → 25
# 98 = 2 * 7 * 7 = 2 * 7^2 → 49
# 242 = 2 * 11 * 11 = 2 * 11^2 → 121
# 338 = 2 * 13 * 13 = 2 * 13^2 → 169

# Какие числа имеют три чётных делителя? Удвоенный квадрат простого числа
import time


def get_even_factors(n):
    return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i) if x % 2 == 0}


start = time.time()
for x in range(106_000_000, 107_000_001):
    # for x in range(1, 10000):
    fs = get_even_factors(x)
    if len(fs) == 3:
        print(x, fs)

    # Прогресс:
    if x % 10000 == 0:
        finish = time.time()
        print("Проверили", x, finish - start)
        start = finish

# for p in range(1, 10000):
#     fs = [i for i in range(1, p + 1) if p % i == 0]
#     x = 2 * p ** 2
#     if len(fs) == 2 and 106_000_000 <= x <= 107_000_000:
#         print(x)
