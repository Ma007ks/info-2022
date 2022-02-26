def q(s, f):
    if s in {13, 15}:  # s == 13 or s == 15
        return 0
    return q(s + 1, f) + q(s + 2, f) + q(s * 3, f) if s < f else s == f


print(q(1, 10) * q(10, 20))
