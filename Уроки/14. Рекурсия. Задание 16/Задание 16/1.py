def f(n):
    if n == 1 or n == 2 or n == 3:
        return 4

    if n % 4 == 0:
        return 5 * f(n - 3)

    return 2 * f(n - 1) + 4 * n


print(f(16))
