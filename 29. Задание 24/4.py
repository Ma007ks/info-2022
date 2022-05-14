s = open("4.txt").read()

for a in "klmnop":
    for b in "klmnop":
        if a != b:
            for length in range(1, 1000):
                w = a + b * length + a
                if w in s and length >= 8:
                    print(length, a, b)
