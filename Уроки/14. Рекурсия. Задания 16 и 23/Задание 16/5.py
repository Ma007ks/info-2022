def f(n):
    if n == 1:
        return 1
    if n % 3 == 0:
        return f(n - 2) // 2
    if n % 3 == 1:
        return f(n - 1) + f(n - 2)
    return 2 * f(n - 1)


print(f(24))
