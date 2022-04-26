for i in range(1, 10000):
    x = i
    a, b = 0, 10
    while x > 0:
        d = x % 6
        if d > a:
            a = d
        if d < b:
            b = d
        x //= 6
    if a * b == 12:
        print(i)
