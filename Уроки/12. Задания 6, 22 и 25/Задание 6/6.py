for i in range(1, 1000):
    s = i
    n = 300
    while s - n > 0:
        s -= 25
        n -= 10
    if n == 150:
        print(i, n)
