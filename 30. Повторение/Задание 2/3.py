for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x <= y) and (y <= z)
            print(x, y, z, int(f))
