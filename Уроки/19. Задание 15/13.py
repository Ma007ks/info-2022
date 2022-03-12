def expr(x, s, f):
    p = 7 <= x <= 14
    q = 9 <= x <= 11
    a = s <= x <= f
    return (p == q) <= (not a)


mx = 0

for s in range(1, 100):
    for f in range(s, 100):
        if all(expr(x + 0.5, s, f) for x in range(-1000, 1000)):
            mx = max(mx, f - s)

print(mx)
