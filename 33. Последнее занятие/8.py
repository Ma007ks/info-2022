def expr(x, s, f):
    p = 43 <= x <= 67
    q = 55 <= x <= 89
    a = s <= x <= f
    return p <= (a or q)


for s in range(1, 100):
    for f in range(1, 100):
        if all(expr(x, s, f) for x in range(1, 1000)):
            if f - s <= 12:
                print(s, f, f - s)
