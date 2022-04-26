def q(s, f):
    if s in [5, 10]:  # s == 5 or s == 10
        return 0
    return q(s + 1, f) + q(s * 2, f) + q(s + 3, f) if s < f else s == f


print(q(2, 14))
