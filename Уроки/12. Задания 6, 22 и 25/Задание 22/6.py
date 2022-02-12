for i in range(1001, 10000, 2):
    x, b, l, m = i, 1, 0, 0
    while x:
        b += 1
        if x % b % 2:
            l += x % b + 1
        else:
            m += x % b + 1
        x //= b
    if l == 8 and m == 5:
        print(i)
