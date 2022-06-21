count = 0

# 01, 03, 05, 07
# 10, 30, 50, 70

for a in range(1, 9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    w = f"{a}{b}{c}{d}{e}"
                    if w.count("0") == 1 and all(v not in w for v in ("01", "03", "05", "07", "10", "30", "50", "70")):
                        count += 1
                        print(count, w)
