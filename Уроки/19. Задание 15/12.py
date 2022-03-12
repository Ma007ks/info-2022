# P = [4; 15]

# x ∈ P: 4 <= x <= 15
# x ∉ P: not 4 <= x <= 15


def expr(x, s, f):
    return ((4 <= x <= 15) and (12 <= x <= 20)) <= (s <= x <= f)


mn = 100000

for s in range(1, 100):
    for f in range(s, 100):
        if all(expr(x + 0.01, s, f) for x in range(-100, 100)):
            mn = min(mn, f - s)

print(mn)
