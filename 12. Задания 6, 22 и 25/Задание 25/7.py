for x in range(850_001, 1_000_000):
    fs = [f for f in range(2, x) if x % f == 0]
    if fs:
        f = fs[-1] - fs[0]  # max(fs) - min(fs)
    else:
        f = 0
    f = fs[-1] - fs[0] if fs else 0
    if f != 0 and f % 11 == 0:
        print(x, f)
