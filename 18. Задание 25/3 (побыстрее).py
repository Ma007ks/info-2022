def get_m(n):
    # fs = {x for f in range(1, int(n ** .5) + 1) if n % f == 0 for x in (f, n // f)}
    fs = set()
    for f in range(1, int(n ** .5) + 1):
        if n % f == 0:
            fs.add(f)
            fs.add(n // f)

    fs = sorted(fs)[1:]

    if len(fs) < 5:
        return 0

    return fs[0] * fs[1] * fs[2] * fs[3] * fs[4]


for n in range(500_000_001, 500_000_020):
    m = get_m(n)
    if 0 < m < n:
        print(n, m)
