for i in range(1, 1000):
    x = i
    a, b = 0, 1
    while x > 0:
        a += 1
        b *= x % 100
        x //= 100
    if a == 2 and b == 7:
        print(a, b, i)
