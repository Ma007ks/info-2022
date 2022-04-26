def f(n):
    if n <= 0:
        return 5
    if n % 2 == 0:
        return g(n - 1) + f(n - 1)
    return g(n - 3)


def g(n):
    if n <= 0:
        return 1
    if n % 3 != 2:
        return f(n - 1) + 2
    return f(n - 2) + 2 * g(n - 3) + 5


print(f(31))
