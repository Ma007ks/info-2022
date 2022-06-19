def q(s, f, last_action=""):
    if s == 3:
        return 0
    if s < f:
        return q(s + 1, f, "+1") + q(s + 3, f, "+3") + q(s * 2, f, "*2")
    return s == f and last_action == "*2"


print(q(1, 30))
# print(q(1, 15))
