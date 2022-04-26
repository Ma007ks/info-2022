def expr(x, s, f):
    p = 17 <= x <= 40
    q = 20 <= x <= 57
    a = s <= x <= f
    return (not a) <= ((p and q) <= a)


mn = 1000000000000000

for s in range(1, 100):
    for f in range(s, 100):
        if all(expr(x + 0.01, s, f) for x in range(1, 1000)):
            mn = min(mn, f - s)

print(mn)
