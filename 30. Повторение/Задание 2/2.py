for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x <= y) and z or (y == z)
            if f == 0:
                print(x, y, z)
