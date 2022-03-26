for n in range(1, 1000):
    r = bin(n)[2:]
    # s = sum(int(d) for d in r)
    s = sum(map(int, r))
    r += str(s % 2)
    s = sum(map(int, r))
    r += str(s % 2)
    r = int(r, 2)
    if r <= 57:
        print(r)
