i = 0

for a in "ABC":
    for b in "ABC":
        for c in "ABC":
            for d in "ABC":
                for e in "ABCX":
                    i += 1
                    # print(i, a + b + c + d + e)

print(i)
