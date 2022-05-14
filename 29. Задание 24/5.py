s = open("5.txt").read()

for a in "abcdefg":
    for b in "abcdefg":
        for c in "abcdefg":
            if len({a, b, c}) == 3:
                for length in range(1, 1000):
                    w = a + b * length + c
                    if length >= 8 and w in s:
                        print(length, a, b, c)
