def expr(x, s, f):
    a = s <= x <= f
    return (a <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= a)


mn = 1000000000000

for s in range(-100, 100):
    for f in range(s, 100):
        if all(expr(x + 0.5, s, f) for x in range(-100, 100)):
            mn = min(mn, f - s)

print(mn)
