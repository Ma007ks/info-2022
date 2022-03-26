for n in range(1, 1000):
    r = bin(n)[2:]
    s = sum(map(int, r))
    r += str(s % 2)
    s = sum(map(int, r))
    r += str(s % 2)
    r = int(r, 2)
    if r > 99:
        print(n)
