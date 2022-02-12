for i in range(1, 1000):
    s = i
    n = 36
    while s < 2020:
        s *= 2
        n += 3
    if n == 60:
        print(i)
