i = 0

for a in "КАТЕР":
    for b in "КАТЕР":
        for c in "КАТЕР":
            for d in "КАТЕР":
                for e in "КАТЕР":
                    w = a + b + c + d + e
                    if w.count("Р") >= 2:
                        i += 1
                        print(i, w)
