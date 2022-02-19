import time
from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10_000)


def fib_loop(n):
    """Находит n-ое число Фибоначчи"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@cache
def fib(n):
    if n <= 100000:
        return fib_loop(n)
    return fib(n - 1) + fib(n - 2)


for n in range(100000, 100050):
    start_time = time.time()
    f = fib(n)
    finish_time = time.time()
    print(f"fib({n}) ({finish_time - start_time})")
