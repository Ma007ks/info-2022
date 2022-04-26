def q(s, f):
    return q(s + 3, f) + q(s + 5, f) + q(s * 2, f) if s < f else s == f


print(q(2, 13) * q(13, 26))
