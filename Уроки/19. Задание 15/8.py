def expr(x, a):
    return (x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0))


for a in range(1000):
    if all(expr(x, a) for x in range(10000)):
        print(a)
        break
