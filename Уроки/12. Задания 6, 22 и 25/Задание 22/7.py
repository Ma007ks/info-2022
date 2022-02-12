for i in range(151, 1000):
    x = i
    n, m = 2 * x - 30, 2 * x + 30
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
    if m == 30:
        print(i)
