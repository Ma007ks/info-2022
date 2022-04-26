def f(n):
    if n < 0:
        return f(n + 2) + 1
    if n == 0:
        return 2
    return f(n - 5) ** 2 - f(n - 3) * f(n - 7)


print(f(24))
