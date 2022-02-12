for initial_x in range(1, 10000):
    for initial_s in range(1, 10000):
        s = initial_s
        x = initial_x
        s = 100 * s + x
        n = 1
        while s < 2021:
            s += 5 * n
            n += 1

        if n == 15:
            print(initial_x, initial_s)
