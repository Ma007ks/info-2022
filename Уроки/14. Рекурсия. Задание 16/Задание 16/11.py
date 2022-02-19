def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 2:
        return f(n - 1) + 1
    return f((n - n % 3) / 3)


for n in range(1, 1000):
    if f(n) == 6:
        print(n)
