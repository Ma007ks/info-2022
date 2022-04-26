n = 2359253

factors = []
count_factors = 0
sum_factors = 0

for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
        count_factors += 1
        sum_factors += i

print(factors)
print(len(factors))
print(count_factors)
print(sum_factors)
print(sum(factors))
