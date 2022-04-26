def algo(n):
    r = bin(n)[2:]
    r = r.replace("0", "00").replace("1", "11")
    # r = "".join(d * 2 for d in r)
    return int(r, 2)


for n in range(1, 10):
    r = algo(n)
    if r > 32:
        print(r)
