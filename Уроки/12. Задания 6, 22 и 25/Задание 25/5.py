for x in range(51120, 89081, 30):
    if x % 30 == 0:
        factors = [
            f
            for f in range(1, x)
            if x % f == 0 and f % 2 == 0 and f % 3 == 0 and f % 5 == 0
        ]
        if len(factors) == 2:
            print(x, factors[0], factors[1])

# x = 30p^2
