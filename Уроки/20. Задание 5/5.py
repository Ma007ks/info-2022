for n in range(1, 1000):
    r = bin(n)[2:]
    r += str(n % 2) * len(r)
    r = int(r, 2)
    if r < 100:
        print(r)
