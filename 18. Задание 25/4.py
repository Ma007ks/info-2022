def get_m(n):
    fs = [f for f in range(1, n) if n % f == 0]

    # fs = set()
    # for f in range(1, int(n ** 0.5) + 1):
    #     if n % f == 0:
    #         fs.add(f)
    #         fs.add(n // f)
    #
    # fs = sorted(fs)[:-1]

    if len(fs) < 2:
        return 0

    return fs[-1] + fs[-2]


for n in range(11_000_001, 12_000_000):
    m = get_m(n)
    if 0 < m < 10_000:
        print(n, m)
