for n in range(1, 1000):
    r = bin(n)[2:]
    s = sum(int(d) for d in r)
    r += str(s % 2)
    s = sum(int(d) for d in r)
    r += str(s % 2)
    r = int(r, 2)
    if r > 126:
        print(r)
