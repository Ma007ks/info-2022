i = 0

# 246
for a in "123456":
    for b in "123456":
        for c in "123456":
            w = a + b + c
            if len(set(w)) == 3 and "2" in w and "4" in w and "6" in w:
                i += 1
                print(i, w)

# 246 + 1 дополнительная
for a in "123456":
    for b in "123456":
        for c in "123456":
            for d in "123456":
                w = a + b + c + d
                if len(set(w)) == 4 and "2" in w and "4" in w and "6" in w:
                    i += 1
                    print(i, w)

# 246 + 2 дополнительных
for a in "123456":
    for b in "123456":
        for c in "123456":
            for d in "123456":
                for e in "123456":
                    w = a + b + c + d + e
                    if len(set(w)) == 5 and "2" in w and "4" in w and "6" in w:
                        i += 1
                        print(i, w)

# 246 + 3 дополнительных
for a in "123456":
    for b in "123456":
        for c in "123456":
            for d in "123456":
                for e in "123456":
                    for f in "123456":
                        w = a + b + c + d + e + f
                        if len(set(w)) == 6 and "2" in w and "4" in w and "6" in w:
                            i += 1
                            print(i, w)
