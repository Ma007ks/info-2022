for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                for k in 0, 1:
                    a = x <= y
                    b = (not z) <= w
                    c = z <= (not y)
                    r = (b and c) or k
                    f = a <= r
                    if f == 0:
                        print(x, y, z, w, k)
