for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                a = ((not x) <= y) <= z
                b = (y <= z) <= (not w)
                c = (z <= (not w)) <= x
                f = a <= (b and c)
                if f == 0:
                    print(x, y, z, w)
