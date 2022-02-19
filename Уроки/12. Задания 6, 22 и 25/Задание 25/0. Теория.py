def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def get_factors(n):
    factors = set()  # []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)  # add, а не append
            factors.add(n // i)
    return sorted(factors)


def get_factors(n):
    return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i)}


def get_non_trivial_factors(n):
    return [i for i in range(2, n) if n % i == 0]


def get_min_factor(x):
    for f in range(2, x):
        if x % f == 0:
            return f


def get_max_factor(x):
    # range(2, x)[::-1]
    # range(x - 1, 1, -1)
    for f in reversed(range(2, x)):
        if x % f == 0:
            return f


# СОВЕТЫ И РЕКОМЕНДАЦИИ:
# 1. Лучше сначала писать программу для маленького диапазона из маленьких чисел.
# 2. Если программа долго работает, запускаем её на маленьких значениях
# и смотрим, каким общим свойством обладают все найденные числа.
