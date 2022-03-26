def algo(n):
    r = bin(n)[2:]
    if n % 4 == 0:
        r += "00"
    if n % 4 == 1:
        r += "01"
    if n % 4 == 2:
        r += "10"
    if n % 4 == 3:
        r += "11"
    return int(r, 2)


for n in range(1, 1000):
    r = algo(n)
    if r < 100:
        print(r)
