def expr(x, s, f):
    p = 10 <= x <= 30
    q = 20 <= x <= 40
    a = s <= x <= f
    return (not a) <= (p <= (not q))


min_count = 100000000000000

for s in range(1, 100):
    for f in range(s, 100):
        if all(expr(x + 0.5, s, f) for x in range(-100, 100)):
            count_odd = sum(i % 2 == 1 for i in range(s, f + 1))
            if count_odd < min_count:
                min_count = count_odd
                print(min_count, s, f)
