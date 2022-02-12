for i in range(1, 10000):
    x = i
    a, b, d = 0, 0, 0
    while x > 0:
        if d % 2 == 0:
            a += x % 10
        else:
            b += x % 10
        x //= 10
        d += 1
    if (a, b) == (3, 16):  # a == 3 and b == 16
        print(i)
