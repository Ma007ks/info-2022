def get_factors(x):
    factors = []
    for i in range(1, abs(x) + 1):
        if x % i == 0:
            factors.append(i)
    return factors


def is_prime(x):
    factors = get_factors(x)
    return len(factors) == 2


for i in range(1, 1000):
    if is_prime(i):
        print(i)
