for n in range(26_600, 28_100 + 1):
    fs = [f for f in range(2, n) if n % f == 0]
    if fs and len(fs) % 13 == 0:
        print(n, len(fs))
