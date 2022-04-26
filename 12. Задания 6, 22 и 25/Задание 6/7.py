for i in range(1, 1000):
    s = i
    n = 80
    while s < 75:
        s += 5
        n -= 4
    if n == 20:
        print(i, n)
