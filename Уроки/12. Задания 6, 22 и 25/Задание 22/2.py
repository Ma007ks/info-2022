for i in range(10000, 100000):
    x = i
    a, b = 0, 0
    while x > 0:
        y = x % 10
        if y > 3:
            a += 1
        if y < 8:
            b += 1
        x //= 10
    if (a, b) == (4, 2):  # a == 4 and b == 2
        print(i)
