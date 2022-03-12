def expr(x, a):
    w = (x % 10 == 0) <= (x % 12 != 0)
    return (a < 50) and ((x % a != 0) <= w)


for a in range(1, 1000):
    if all(expr(x, a) for x in range(1, 10000)):
        print(a)
