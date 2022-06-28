def expr(x, s, f):
    b = 17 <= x <= 25
    c = 10 <= x <= 20
    a = s <= x <= f
    return a or b or not c


for s in range(1, 100):
    for f in range(1, 100):
        if all(expr(x + .5, s, f) for x in range(1, 100)):
            if f - s <= 7:
                print(s, f, f - s)
