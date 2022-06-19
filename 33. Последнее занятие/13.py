from functools import cache


@cache
def q(s, f, last_action="", second_last_action=""):
    if s == 5:
        return 0
    if s < f:
        return (
            q(s + 1, f, "+1", last_action)
            + q(s + 2, f, "+2", last_action)
            + q(s * 3, f, "*3", last_action)
        )
    return s == f and second_last_action == "*3"


print(q(1, 50))
# print(q(1, 15))
