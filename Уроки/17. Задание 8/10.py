i = 0

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    if len({a, b, c, d, e}) != 5:
                        i += 1
                        print(i, a, b, c, d, e)
