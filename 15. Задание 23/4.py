def q(s, f):
    return q(s + 3, f) + q(s + 5, f) + q(s * 2, f) if s < f else s == f


print(q(7, 15) * q(15, 33) * q(33, 50))
