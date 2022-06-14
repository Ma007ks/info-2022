def q(s, f):
    if s in {10, 11}:
        return 0
    return q(s + 1, f) + q(s + 2, f) + q(s * 3, f) if s < f else s == f


print(q(1, 8) * q(8, 27))
