def q(s, f):
    if s > f:
        return q(s - 1, f) + q(s // 2, f)
    return s == f


print(q(30, 12) * q(12, 1))
