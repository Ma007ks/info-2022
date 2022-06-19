def expr(x, a):
    m = (x & 28 != 0) or (x & 45 != 0)
    n = (x & 17 == 0) <= (x & a != 0)
    return m <= n


for a in range(100):
    if all(expr(x, a) for x in range(1000)):
        print(a)
