def fact_loop(n):
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p


def fact(n):
    return fact(n - 1) * n if n >= 2 else 1


print(fact_loop(30))
print(fact(30))
