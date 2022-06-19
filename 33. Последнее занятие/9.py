def expr(x, s, f):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = s <= x <= f
    return (p == q) <= (not a)


for s in range(1, 100):
    for f in range(1, 100):
        if all(expr(x + 0.5, s, f) for x in range(-100, 100)):
            if f - s >= 8:
                print(s, f, f - s)
