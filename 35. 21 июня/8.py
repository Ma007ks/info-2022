count = 0

for a in range(1, 8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    # w = str(a) + str(b) + str(c) + str(d) + str(e)
                    w = f"{a}{b}{c}{d}{e}"
                    if a % 2 == 0 and e != 3 and e != 4 and w.count("5") <= 0:
                        count += 1
                        print(count, w)
