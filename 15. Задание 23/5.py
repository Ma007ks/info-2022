def q(s, f):
    if s == 55:
        return 0
    return q(s + 1, f) + q(s * 2, f) + q(s * 3, f) if s < f else s == f


print(q(32, 125))
