i = 0

for a in "ИВАН":
    for b in "ИВАН":
        for c in "ИВАН":
            for d in "ИВАН":
                for e in "ИВАН":
                    w = a + b + c + d + e
                    if w.count("И") >= 1:
                        i += 1
                        print(i, w)

print(i)
