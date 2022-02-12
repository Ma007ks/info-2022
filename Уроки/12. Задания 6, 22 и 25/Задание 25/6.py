for n in range(700_001, 700_100):
    fs = [f for f in range(2, n) if n % f == 0]
    # if len(fs) > 0:  # if fs:
    #     m = fs[0] + fs[-1]
    # else:
    #     m = 0
    m = fs[0] + fs[-1] if fs else 0
    if m % 10 == 8:
        print(n, m)
