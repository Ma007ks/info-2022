s = open("24.txt").read()
print(len(s))

for a in "klmnop":
    for b in "klmnop":
        if a != b:
            for length in range(1, 10000):
                substring = a + b * length + a
                if substring in s:
                    if length >= 8:
                        print(a, b, length)
