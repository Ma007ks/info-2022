i = 0

for a in "СОН":
    for b in "СОН":
        for c in "СОН":
            for d in "ОН":
                for e in "ОН":
                    for f in "ОН":
                        w = a + b + c + d + e + f
                        if w.count("С") != 2:
                            i += 1
                            print(i, w)
