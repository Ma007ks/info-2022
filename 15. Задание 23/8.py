def q(s, f):
    return q(s + 1, f) + q(s * 3, f) + q(2 * s - 1, f) if s < f else s == f


print(q(3, 12) * q(12, 37))
