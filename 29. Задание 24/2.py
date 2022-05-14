s = open("2.txt").read()

for d in "0123456789":
    for length in range(1, 10000):
        if d * length not in s:
            break
    print(d, length - 1)
