for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in (1,):
                for k in (0,):
                    a = (x != y) == ((z <= x) or not y)
                    f = a or (w <= k)
                    if f == 1 and 2 <= x + y + z + w + k <= 3:
                        print(x, y, z, w, k)
