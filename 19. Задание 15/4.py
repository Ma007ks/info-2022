def expr(x, y, a):
    z = (2 * x + 5 * y <= 18) <= (2 * x + y < a)
    w = (5 * x + 3 * y <= 25) <= (2 * x + y < a)
    return z <= (not w)


for a in range(1, 1000):
    if all(not expr(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
