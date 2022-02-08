n = 470

factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

print(factors)

factors = [i for i in range(1, n + 1) if n % i == 0]
factors = {i for i in range(1, n + 1) if n % i == 0}

print(factors)
