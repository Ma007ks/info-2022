for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x <= y) and (y <= z)
            if f == 1:
                print(x, y, z, f)
