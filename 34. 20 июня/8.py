count = 0

for a in "АЛПЦЯ":
    for b in "АЛПЦЯ":
        for c in "АЛПЦЯ":
            for d in "АЛПЦЯ":
                for e in "АЛПЦЯ":
                    w = a + b + c + d + e
                    count += 1
                    # if w.count("А") <= 1 and "Л" not in w and w.count("Ц") == 2:
                    print(count, w)
