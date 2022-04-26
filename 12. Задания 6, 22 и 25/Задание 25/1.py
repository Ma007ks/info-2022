# factors = [i for i in range(2, n) if n % i == 0]
for n in range(174457, 174505 + 1):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    if len(factors) == 2:
        print(n, factors, factors[0] * factors[1])

# for n in range(1, 101):
#     fs = [i for i in range(2, n) if n % i == 0]
#     if len(fs) == 2:
#         print(n, fs, fs[0] * fs[1])
