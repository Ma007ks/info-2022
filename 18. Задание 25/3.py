def get_m(n):
    fs = [f for f in range(2, n + 1) if n % f == 0]

    if len(fs) < 5:
        return 0

    return fs[0] * fs[1] * fs[2] * fs[3] * fs[4]


for n in range(500_000_001, 600_000_000):
    print("Проверяем", n)
    m = get_m(n)
    if 0 < m < n:
        print(n, m)
