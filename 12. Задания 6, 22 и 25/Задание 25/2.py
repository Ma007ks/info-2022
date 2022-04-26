for n in range(3954, 8979 + 1):
    factors = [f for f in range(1, n + 1) if n % f == 0]
    if 41 <= len(factors) <= 45:
        print(n, len(factors))
