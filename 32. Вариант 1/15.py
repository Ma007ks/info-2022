def expr(x, s, f):
    p = 17 <= x <= 54
    q = 37 <= x <= 83
    a = s <= x <= f
    return p <= ((q and (not a)) <= (not p))


for s in range(1, 100):
    for f in range(1, 100):
        if all(expr(x + 0.1, s, f) for x in range(-100, 100)):
            if f - s <= 18:
                print(s, f, f - s)
