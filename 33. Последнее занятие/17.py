def gf(n):
    return [f for f in range(1, n + 1) if n % f == 0]


# for x in range(650001, 650500):
#     ...

for x in range(222223, 260000):
    factors = gf(x)
    sum_odds_factors = sum(f for f in factors if f % 2 != 0)
    # second_max_factor = factors[-2]
    sum_factors = gf(sum_odds_factors)
    if len(sum_factors) == 2:
        print(x, factors, sum_odds_factors)
