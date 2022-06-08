for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                for k in 0, 1:
                    for s in 0, 1:
                        f = ((((x <= y) <= z) <= w) <= k) <= s
                        if f == 0:
                            print(x, y, z, w, k, s)
