def get_factors(n):
    factors = set()  # []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)  # add, а не append
            factors.add(n // i)
    return sorted(factors)


def get_factors(n):
    return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i)}


# def get_factors(n):
#     return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i)}


def get_factors(n):
    return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i)}


# def get_factors(n):
#     return {x for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for x in (i, n // i)}


print(get_factors(36))
