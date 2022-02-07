def nth_fibonacci(n):
    """Находит n-ое число Фибоначчи"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


a, b = 0, 1
n = 0
while a <= 10 ** 100:
    a, b = b, a + b
    n += 1

print(a, n)
print(nth_fibonacci(n))
