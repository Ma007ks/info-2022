print("x y z w f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                a = (not x) or y or z
                b = (not y) and z and w
                f = a == b
                if f == 1:
                    print(x, y, z, w, int(f))
