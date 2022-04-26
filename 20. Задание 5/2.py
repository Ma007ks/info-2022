def algo(n):
    r = n - n % 4
    r = bin(r)[2:]
    r += str(sum(int(d) for d in r) % 2)
    r += str(sum(int(d) for d in r) % 2)
    return int(r, 2)


for n in range(1, 100):
    r = algo(n)
    if r > 56:
        print(r)
