for i in range(1, 100000000):
    x = i
    a, b = 1, 0
    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d
        x //= 10

    if a == 6300:
        print(i, b)
