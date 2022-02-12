for x in range(123_040, 123_081):
    even_factors = [f for f in range(2, x) if x % f == 0 and f % 2 == 0]
    if len(even_factors) == 3:
        print(x, even_factors)
