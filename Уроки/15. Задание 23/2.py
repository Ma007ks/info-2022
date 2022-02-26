def q(s, f):
    return q(s + 1, f) + q(s * 2, f) + q(s * 3, f) if s < f else s == f


def q(s, f):
    if s == f:
        return 1
    if s > f:
        return 0
    if s < f:
        return q(s + 1, f) + q(s * 2, f) + q(s * 3, f)


print(q(5, 30))
