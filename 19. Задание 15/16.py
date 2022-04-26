def expr(x, s, f):
    p = 10 <= x <= 35
    q = 17 <= x <= 48
    a = s <= x <= f
    return (a <= (not p)) <= (a <= q)


mx = 0

for s in range(1, 100):
    for f in range(s, 100):
        if all(expr(x + 0.0, s, f) for x in range(1, 1000)):
            mx = max(mx, f - s)

print(mx)
