for i in range(101, 10000):
    x = i
    n, m = x - 30, x + 30
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
    if m == 60:
        print(i)
