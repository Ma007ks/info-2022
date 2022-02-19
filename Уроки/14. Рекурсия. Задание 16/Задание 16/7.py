def f(n):
    if n == 1 or n == 2:
        return n
    if n % 2 == 0:
        # return int((7 * n + f(n - 3)) // 9)
        return (7 * n + f(n - 3)) // 9
    return int((5 * n + f(n - 1) + f(n - 2)) / 7)


for n in range(1, 100):
    print(f"f({n}) = {f(n)}")
