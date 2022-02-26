def q(s, f):
    """Считает количество программ, которые число s
    преобразовывают в число f"""

    if s < f:
        return q(s + 1, f) + q(s + 2, f)

    # s >= f
    if s == f:
        return 1

    if s > f:
        return 0


def q(s, f):
    if s < f:
        return q(s + 1, f) + q(s + 2, f)
    return s == f


def q(s, f):
    return q(s + 1, f) + q(s + 2, f) if s < f else s == f


for s in range(1, 15):
    print(f"q({s}, 11) = {q(s, 11)}")
